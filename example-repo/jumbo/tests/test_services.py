import unittest
import random
import string

from jumbo.core import clusters, nodes, services
from jumbo.utils import session as ss, exceptions as ex


class TestServices(unittest.TestCase):
    def setUp(self):
        self.c_name = 'unittest' + ''.join(random.choices(
            string.ascii_letters + string.digits,
            k=5))
        self.m_names = ['master', 'master',
                        'sidemaster_edge', 'worker', 'ldap']
        clusters.create_cluster(domain=None,
                                cluster=self.c_name)
        print('\n\nCluster "%s" created' % self.c_name)

        for i, n in enumerate(self.m_names):
            nodes.add_node(name=n + str(i),
                           ip='10.10.10.1%d' % (i + 1),
                           ram=2048,
                           types=n.split('_'),
                           cpus=1,
                           cluster=self.c_name)
        print('%d nodes created' % i)

    def tearDown(self):
        clusters.delete_cluster(cluster=self.c_name)
        print('Cluster deleted')

    def test_add_indep_services(self):
        print('Test "add_indep_services"')
        indep_serv = [s for s in services.config['services']
                      if not s['requirements']['services']['default']]
        for s in indep_serv:
            print('Adding "%s"' % s['name'])
            services.add_service(name=s['name'],
                                 cluster=self.c_name)
        for s in indep_serv:
            self.assertTrue(services.check_service_cluster(s['name']))

    def test_add_indep_services_ha(self):
        print('Test "add_indep_services_ha"')
        indep_serv = [s for s in services.config['services']
                      if not s['requirements']['services']['ha']]
        for s in indep_serv:
            print('Adding "%s"' % s['name'])
            services.add_service(name=s['name'],
                                 ha=True,
                                 cluster=self.c_name)
        for s in indep_serv:
            self.assertTrue(services.check_service_cluster(s['name']))

    def test_add_all_services_auto(self):
        print('Test "add_all_services_auto"')
        for s in services.config['services']:
            self.recursive_add(s['name'], False)
        for s in services.config['services']:
            self.assertEqual(
                services.check_service_complete(name=s['name'],
                                                cluster=self.c_name), [])

    def test_add_remove_all_services_auto(self):
        print('Test "add_remove_all_services_auto"')
        for s in services.config['services']:
            self.recursive_add(s['name'], False)
        for s in ss.svars['services']:
            self.recursive_remove(s)
        for s in services.config['services']:
            self.assertFalse(services.check_service_cluster(name=s['name']))

    def test_add_all_services_auto_ha(self):
        print('Test "add_all_services_auto_ha"')
        installed = []
        for s in services.config['services']:
            try:
                self.recursive_add(s['name'], True)
            except ex.CreationError as e:
                if e.type == 'NotSupported':
                    print(e.message)
                    print('Adding "%s" in default mode' % s['name'])
                    services.remove_service(service=s['name'],
                                            cluster=self.c_name)
                    self.recursive_add(s['name'], False)
                else:
                    raise e
            installed.append(s['name'])
        for s in installed:
            self.assertEqual(
                services.check_service_complete(name=s,
                                                cluster=self.c_name), [])

    def test_add_service_recursive(self):
        print('Test "add_service_recursive"')
        for s in reversed(services.config['services']):
            if s['name'] not in ss.svars['services']:
                print('Recursively adding "%s"' % s['name'])
                services.install_dependencies(
                    dependencies=services.get_service_dependencies(
                        s['name'],
                        first=True,
                        cluster=self.c_name),
                    cluster=self.c_name)
        for s in ss.svars['services']:
            self.recursive_remove(s)
        for s in services.config['services']:
            self.assertFalse(services.check_service_cluster(name=s['name']))

    def recursive_add(self, service, ha):
        if not services.check_service_cluster(service):
            m_serv, _ = services.check_service_req_service(service, ha)
            for serv in m_serv:
                self.recursive_add(serv, ha)

            print('Adding "%s"' % service)
            services.add_service(name=service,
                                 ha=ha,
                                 cluster=self.c_name)
            services.auto_assign(service=service,
                                 ha=ha,
                                 cluster=self.c_name)

    def recursive_remove(self, service):
        if services.check_service_cluster(service):
            dep = services.check_dependent_services(service)
            for s in dep:
                self.recursive_remove(s)

            print('Removing "%s"' % service)
            services.remove_service(service=service,
                                    cluster=self.c_name)


if __name__ == '__main__':
    unittest.main()
