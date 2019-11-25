from ansiblemetrics.general import bloc, cloc, dpt, etp, loc, ndk, nfl, \
                                    nicd, nlk, nlo, nnnv, nnwv, nun
from ansiblemetrics.tasks import atss, nbeh, nbl, ncmd, ndm, nemd, nfmd, nierr, \
                                 nimpr, nimpt, ninc, nincr, ninct, nincv, \
                                 nlp, nmd, nsh, ntnn, ntun
from functions import load


def get_metrics_from_file(file):
    counts = {'atss_count': atss.ATSS(load(file)).count(),
              'bloc_count': bloc.BLOC(load(file)).count(),
              'bloc_count_rel': bloc.BLOC(load(file)).count(relative=True),
              'cloc': cloc.CLOC(load(file)).count(),

              'cloc_count_rel': cloc.CLOC(load(file)).count(relative=True),
              'dpt_count': dpt.DPT(load(file)).count(),
              'etp_count': etp.ETP(load(file)).count(),
              'loc_count': loc.LOC(load(file)).count(),

              'nbeh_count': nbeh.NBEH(load(file)).count(),
              'nbeh_count_rel': nbeh.NBEH(load(file)).count(relative=True),
              'nbl': nbl.NBL(load(file)).count(),

              'ncmd': ncmd.NCMD(load(file)).count(),


              'ndk_count': ndk.NDK(load(file)).count(),
              'ndk_occurrences': ndk.NDK(load(file)).count(occurrences=True),
              'ndm': ndm.NDM(load(file)).count(),

              'ndm_occurrences': ndm.NDM(load(file)).count(occurrences=True),
              'nemd_count_rel': nemd.NEMD(load(file)).count(relative=True),
              'nfl_count': nfl.NFL(load(file)).count(),

              'nfmd_count': nfmd.NFMD(load(file)).count(),
              'nfmd_count_rel': nfmd.NFMD(load(file)).count(relative=True),
              'nicd_count': nicd.NICD(load(file)).count(),
              'nierr_count': nierr.NIERR(load(file)).count(),

              'nimpr_count': nimpr.NIMPR(load(file)).count(),
              'nimpt_count': nimpt.NIMPT(load(file)).count(),
              'ninc_count': ninc.NINC(load(file)).count(),
              'nincr_count': nincr.NINCR(load(file)).count(),

              'ninct_count': ninct.NINCT(load(file)).count(),
              'nincv_count': nincv.NINCV(load(file)).count(),
              'nlk_count': nlk.NLK(load(file)).count(),
              'nlo_count': nlo.NLO(load(file)).count(),
              'nlp_count': nlp.NLP(load(file)).count(),

              'nmd_count': nmd.NMD(load(file)).count(),
              'nnnv_count_rel': nnnv.NNNV(load(file)).count(relative=True),
              'nnwv_count': nnwv.NNWV(load(file)).count(),
              'nnwv_count_rel': nnwv.NNWV(load(file)).count(relative=True),

              'nsh_count': nsh.NSH(load(file)).count(),
              'ntnn_count': ntnn.NTNN(load(file)).count(),
              'ntun_count_rel': ntun.NTUN(load(file)).count(relative=True),
              'nun_count_rel': nun.NUN(load(file)).count(relative=True)}
    return counts
