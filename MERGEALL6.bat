python MergeModels.py num12 num22
python MergeModels.py num12 num32
python MergeModels.py num12 num42
python MergeModels.py num12 num52
python MergeModels.py num12 num62

echo "deleting old merge files"

del num22
del num32
del num42
del num52
del num62

del num11
del num21
del num31
del num41
del num51
del num61

copy num12 num22 /B
copy num12 num32 /B
copy num12 num42 /B
copy num12 num52 /B
copy num12 num62 /B