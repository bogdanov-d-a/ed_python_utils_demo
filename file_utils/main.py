from edpu import file_utils

file_utils.create_and_open_dir_with_datetime('.')
print(file_utils.eval_file('eval.txt'))
