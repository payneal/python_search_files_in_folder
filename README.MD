# how to use: checking if value in file

* add class to file
```python
    from check_folder import Check_Folder

    check = Check_Folder()
```

* check a directory for everyfile with certain string
```python
    
    strings_to_locate = [
        'all', 
        'strings', 
        'you', 
        'want', 
        'to', 
        'search', 
        'for']
    directory_location = './directory/you/want/to/search'

    answer = check.check_if_list_in_files(
            strings_to_locate, directory_location)

    print answer

    # will look something like this 
    # [] == no files in that directory with that string
    # currently doesnt account for caps/not caps

    { 
        'all': {
            'files': [
                './directory/you/want/to/search/one.py',
                './directory/you/want/to/search/two.py',
                './directory/you/want/to/search/one.txt',
            ]},
        'strings': {
             'files': []},
        'you': {
             'files': []},
        'want': {
             'files': []},
        'to': {
             'files': []},
        'search': {
             'files': []},
        'for': { 
            'files': []}
    }

```

* see test file for more examples 
