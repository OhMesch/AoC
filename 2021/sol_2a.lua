-- Open input file
local this_file_info = debug.getinfo(1, "S").source:sub(2)
local file_name = this_file_info:match("_([^.]*).")
local input_file = "input_" .. file_name:sub(1, #file_name-1) .. ".txt"

-- Populate input data array
local input_data = {}
for line in io.lines(input_file) do
	input_data[#input_data+1] = line
end

-- Start of problem specific code
local position = {["forward"] = 0,
                  ["up"] = 0,
                  ["down"] = 0}
for _, direction_command in pairs(input_data) do
	for d,v in string.gmatch(direction_command, "(%a+) (%d+)") do
		position[d] = position[d] + tonumber(v)
	end
end

print(position["forward"]*(position["down"]-position["up"]))
