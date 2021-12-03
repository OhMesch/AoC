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
local aim = 0
local depth = 0
local horizontal = 0

for _, direction_command in pairs(input_data) do
	for direction, value in string.gmatch(direction_command, "(%a+) (%d+)") do
		value = tonumber(value)
		if direction == "forward" then
			horizontal = horizontal + value
			depth = depth + aim * value
		elseif direction == "down" then aim = aim + value
		elseif direction == "up" then aim = aim - value
		end
	end
end

print(horizontal*depth)
