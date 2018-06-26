#!/usr/bin/env python3

# TODO move into test harness when appropriate

import ukcensusapi.NISRA as NISRA

census = NISRA.NISRA("~/.ukpopulation/cache")

print(census.area_lookup.head())

# meta = census.get_metadata("KS401SC", "LAD")
# print(meta)

# KS401 no data at LSOA level, yet there is data at OA?
# compression format of OA data not supported by zipfile

# data = census.get_data("KS401SC", "LAD", "S92000003", category_filters={"KS401SC_0_CODE": 0})
# print(data.head())
# meta = census.get_metadata("DC1117SC", "LAD")
# print(meta)
# meta = census.get_metadata("DC2101SC", "LAD")
# print(meta)

# table = census.get_data("KS402SC", "MSOA11", "S12000033", category_filters={"KS402SC_0_CODE": 0})
# print(len(table) == 49)
# table = census.get_data("KS402SC", "LSOA11", "S12000033", category_filters={"KS402SC_0_CODE": 0})
# print(len(table) == 283)
# table = census.get_data("KS402SC", "OA11", "S12000033", category_filters={"KS402SC_0_CODE": 0})
# print(len(table) == 1992)

# table = census.get_data("DC1117SC", "LAD", "S12000033")
# print(table)

# table = census.get_data("DC2101SC", "LAD", "S12000033", category_filters={
#   "DC2101SC_0_CODE": 4, # white irish
#   "DC2101SC_1_CODE": [1,2], # male & female
#   "DC2101SC_2_CODE": range(6,13) # 18-49
#   })
# print(table.shape)

# table = census.contextify(table, meta, "DC2101SC_2_CODE")
# print(table)

# # this table has comma thousands separator in raw data
# meta = census.get_metadata("KS201SC", "LAD")
# print(meta)
# data = census.get_data("KS201SC", "LAD", "S12000033")#, category_filters={"DC2101SC_1_CODE": [0], "DC2101SC_2_CODE": 0})
# print(data)
