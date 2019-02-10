# hunalign-wrapper
A set of scripts to build parallel corpora using hunalign<br><br>

###Usage
######File system structure:
<pre><code>
${corpus_title}
|-- source
    |-- snt
            ${title}_${lang}.snt
|-- work
    |-- ${source_lang}-${target_lang}
            ${title}_${lang}.snt.aligned
|-- aligned_idx
    |-- ${source_lang}-${target_lang}
            ${title}.${lang}.idx
|-- result
        ${corpus_title}.${source_lang}-${target_lang}.${source_lang}
        ${corpus_title}.${source_lang}-${target_lang}.${target_lang}
        ${corpus_title}.unique.${source_lang}-${target_lang}.${source_lang}
        ${corpus_title}.unique.${source_lang}-${target_lang}.${target_lang}
</code></pre>

* Additional dependency: PyYAML. Install it using the `python -m pip install PyYAML` command if necessary.
* Before running the shell script, put your source files in _${corpus\_title}/source/snt_ directory.
* The content of source files must be segmented in sentences (one sentence per line).
* Filenames of input files must have the following pattern: _${title}\_${lang}.snt_ (e.g. _document\_en.snt_).
* Parallel files must have identical titles (e.g. _article\_001\_en.snt_, _article\_001\_fr.snt_).
* _hunalign_batch.txt_ will be created automatically during alignment process. Only specify the desired path (the parent directory must exist).
* _null.dic_ is an empty file. It must exist before running the shell script.
* There are two source data directories - _'original_source_data_directory'_ and _'source_data_directory'_ specified in the YAML file.
The 'original_source_data_directory' is used for files containing sentences in natural language or unmodified sentences.
The _'source_data_directory'_ is used for additionaly preprocessed files from the 'original_source_data_directory' e.g. stemmed files.
In both directories, files must be stored in the _'snt'_ subfolder.
The sentence alignment is done using the content from the _'source_data_directory'_.
On the contrary, the building of parallel corpora is done using the content from _'original_source_data_directory'_.
If no additional preprocessing has been made on source files, both paths must be equal.
* The _'work'_, _'aligned_idx'_ and _'result'_ directories are created automatically.
* Aligned corpora are placed in the _'result'_ directory.<br>

######An example of a configuration file (YAML):
(for running on Windows OS; replace ellipsis in brackets with actual paths; see also _io\_args.yml.sample_)
<pre><code>
source_language: en
target_language: fr

corpus_title: aligned_corpora
batch_filepath: [...]\aligned_corpora\hunalign_batch.txt

hunalign_exe: /path/to/hunalign/binary
hunspell_null_dic: /path/to/hunspell\null.dic

original_source_data_directory: [...]\aligned_corpora\source
source_data_directory: [...]\aligned_corpora\source
work_directory: [...]\aligned_corpora\work
alignment_index_directory: [...]\aligned_corpora\aligned_idx
output_data_directory: [...]\aligned_corpora\result

alignment_threshold: 0
</code></pre>


####Running the shell script

Execute the following command (on Windows):<br>
`.\run_hunalign.bat io_args.yml`
<br><br>
__Note:__ The current set of scripts may be also run under UNIX/Linux OS.
For this purpose, a Bash file similar to _run\_hunalign.bat_ must be executed.
<hr>

######References:
* [hunalign](https://github.com/danielvarga/hunalign)
* [hunalign (a version for MinGW-w64)](https://github.com/janissl/hunalign)
