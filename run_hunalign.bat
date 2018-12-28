@echo off

set config_file=io_args.yml

echo 1. Building a batch file...
python create_batch_file.py %config_file% || goto ERR

echo 2. Aligning sentences...
python do_segment_alignment.py %config_file% || goto ERR

echo 3. Exporting aligned sentences...
python export_aligned_sents.py %config_file% || goto ERR

echo 4. Finding aligned sentence indices in the original segmented files...
python get_segment_alignments.py %config_file% || goto ERR

echo 5. Building parallel corpora...
python build_parallel_corpora.py %config_file% || goto ERR

echo 6. Extract unique segment pairs...
python extract_unique_pairs.py %config_file% || goto ERR

echo Done.
exit /b

:ERR
echo.
echo ERROR: Process aborted!
exit /b 1
