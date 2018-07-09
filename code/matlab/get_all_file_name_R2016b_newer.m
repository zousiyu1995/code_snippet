% get all file name in current dir and sub dir, Compatible with MATLAB R2016b and newer
function file_list = get_all_file_name_R2016b_newer(path)

dir_data = dir(path);
file_list = dir_data(~[dir_data.isdir]);  % file name of current dir

% get sub dir information
sub_dir = dir_data([dir_data.isdir]);  % struct
dot_dir = ismember({sub_dir.name}, {'.', '..'});  % logical
sub_dir = sub_dir(~dot_dir);  % struct, remove specific folder

% recursion
for i = 1:length(sub_dir)
    next_dir = fullfile(sub_dir(i).folder, sub_dir(i).name);  % str
    file_list = [file_list; get_all_file_name_R2016b_newer(next_dir)];  % struct
end

end