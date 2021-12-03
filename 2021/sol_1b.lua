-- Open input file
local this_file_info = debug.getinfo(1, "S").source:sub(2)
local file_name = this_file_info:match("_([^.]*).")
local input_file = "input_" .. file_name:sub(1, #file_name-1) .. ".txt"

-- Populate input data array
input_data = {}
for line in io.lines(input_file) do
	input_data[#input_data+1] = line
end

-- Start of problem specific code
inc_count = 0
for i=4,#input_data do
	if tonumber(input_data[i]) > tonumber(input_data[i-3]) then inc_count = inc_count + 1 end
end

print(inc_count)
