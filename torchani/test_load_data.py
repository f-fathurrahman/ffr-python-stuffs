import os
import sys
import torch
import my_torchani

torch.manual_seed(1234) # for reproducibility

dspath = "/home/efefer/WORKS/TORCHANI/torchani-master/dataset/ani1-up_to_gdb4/ani_gdb_s01.h5"
dataset = my_torchani.data.load(dspath)

DATASET_LIST = []

for i,v in enumerate(dataset):
    DATASET_LIST.append(v)
print("Length DATASET_LIST = ", len(DATASET_LIST))
print("Sizeof DATASET_LIST = ", sys.getsizeof(DATASET_LIST))


#

energy_shifter = my_torchani.utils.EnergyShifter(None)
species_order = ["H", "C", "N", "O"]
dataset = my_torchani.data.load(dspath).subtract_self_energies(energy_shifter, species_order).species_to_indices(species_order)

DATASET_LIST2 = []
for i,v in enumerate(dataset):
    DATASET_LIST2.append(v)

print("Ndata DATASET_LIST2  = ", len(DATASET_LIST2))
print("Sizeof DATASET_LIST2 = ", sys.getsizeof(DATASET_LIST2))
 
#
training, validation = my_torchani.data.load(dspath).subtract_self_energies(energy_shifter, species_order).species_to_indices(species_order).shuffle().split(0.8, None)

DATASET_TRAINING = []
for i,v in enumerate(training):
    DATASET_TRAINING.append(v)

DATASET_VAL = []
for i,v in enumerate(validation):
    DATASET_VAL.append(v)
