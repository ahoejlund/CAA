"""
Doc string goes here.

@author: mje mads [] cnru.dk
"""
import mne
# import subprocess
import sys
import glob

from my_settings import *

subject = sys.argv[1]


raw_fname = save_folder + "%s_filtered_ica_mc_raw_tsss.fif" % subject
trans_fname = mne_folder + "%s-trans.fif" % subject
cov = mne.read_cov(mne_folder + "%s-cov.fif" % subject)
bem = glob.glob(mne_folder + "%s-8192-8192*sol.fif" % subject)[0]
src = subjects_dir + "%s/bem/%s-oct-6-src.fif" % (subject, subject)

raw = mne.io.Raw(raw_fname)
raw.del_proj(0)

raw.add_eeg_average_proj()

# src = mne.setup_source_space(subject,
#                              mne_folder + "%s-all-src.fif" % subject,
#                              spacing="all",
#                              subjects_dir=subjects_dir,
#                              n_jobs=1,
#                              overwrite=True)  # 1 for each hemispere

fwd = mne.make_forward_solution(raw_fname, trans=trans_fname,
                                src=src,
                                bem=bem,
                                meg=True,
                                eeg=True,
                                fname=mne_folder + "%s-fwd.fif" % subject,
                                overwrite=True)
