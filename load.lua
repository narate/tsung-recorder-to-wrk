local cjson = require 'cjson'
local f = io.open('wrk_data.json')

local data = f:read('*a')
f:close()

requests = cjson.decode(data)

if #requests <= 0 then
    print("multiplerequests: No requests found.")
    os.exit()
end

local counter = 1
 
request = function()
    -- Get the next requests array element
    local request_object = requests[counter]
    
    -- Increment the counter
    counter = counter + 1
  
    -- If the counter is longer than the requests array length then reset it
    if counter > #requests then
      counter = 1
    end

    -- Return the request object with the current URL path
    return wrk.format(request_object.method, request_object.path, request_object.headers, request_object.body)
end

