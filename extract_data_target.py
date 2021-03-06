# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 12:58:36 2016

@author: mje
"""

from my_settings import *
import mne
import numpy as np
import pandas as pd

epochs = mne.read_epochs(epochs_folder + "0005_target-epo.fif",
                         preload=False)
times = epochs.times


from_time = np.abs(times + 0.1).argmin()
to_time = np.abs(times - 0.1).argmin()

sides = ["left", "right"]
conditions = ["ctl", "ent"]
rois = ["lh", "rh"]
corr = ["correct", "incorrect"]
phase = ["in_phase", "out_phase"]

columns_keys = ["subject", "condition_type", "condition_side", "ROI",
                "correct", "mean"]
df = pd.DataFrame(columns=columns_keys)

for subject in subjects_select:
    for condition in conditions:
        for side in sides:
            for roi in rois:
                for cor in corr:
                    for p  in phase:
                        data = np.load(tf_folder +
                                       "%s_pow_%s_%s_MNE_%s_%s_Brodmann.17-%s_target.npy" %
                                       (subject,
                                        condition,
                                        side,
                                        cor,
                                        p,
                                        roi))
                        data = data[:, :, from_time:to_time].mean()
                        
                        row = pd.DataFrame([{"subject": subject,
                                             "condition_type": condition,
                                             "condition_side": side,
                                             "ROI": roi,
                                             "correct": cor,
                                             "phase": p,
                                             "power": data}])
                        df = df.append(row, ignore_index=True)

df.to_csv(data_path + "alpha_mean_pow_data_extracted_phase_target.csv", index=False)


df = pd.DataFrame(columns=columns_keys)

for subject in subjects_select:
    for condition in conditions:
        for side in sides:
            for roi in rois:
                for cor in corr:
                    for p in phase:
                        data = np.load(tf_folder +
                                       "%s_itc_%s_%s_MNE_%s_%s_Brodmann.17-%s_target.npy" %
                                       (subject,
                                        condition,
                                        side,
                                        cor,
                                        p,
                                        roi))
                        data = data[:, :, from_time:to_time].mean()
                        row = pd.DataFrame([{"subject": subject,
                                             "condition_type": condition,
                                             "condition_side": side,
                                             "ROI": roi,
                                             "correct": cor,
                                             "phase": p,
                                             "itc": data}])
                        df = df.append(row, ignore_index=True)

df.to_csv(data_path + "alpha_mean_itc_data_extracted_phase_target.csv", index=False)
