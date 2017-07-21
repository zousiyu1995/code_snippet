% 获取全部文件夹内的文件
function file_list = get_all_file_name(path)
    dir_data = dir(path);
    file_list = dir_data(~[dir_data.isdir]);  % 当前文件夹下所有文件
    
    % 获取子文件夹
    sub_dir = dir_data([dir_data.isdir]);  % struct
    dot_dir = ismember({sub_dir.name}, {'.', '..'});  % logical
    sub_dir = sub_dir(~dot_dir);  % struct，不含特殊文件夹的所有子文件夹
    
    % 递归
    for i = 1:length(sub_dir)
        next_dir = fullfile(sub_dir(i).folder, sub_dir(i).name);  % str
        file_list = [file_list; get_all_file_name(next_dir)];  % struct
    end
end



