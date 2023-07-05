#!/usr/bin/env ruby
def extract_message_info(log)
  regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
  match = log.match(regex)
  if match
    sender = match[1]
    receiver = match[2]
    flags = match[3]
    puts "#{sender},#{receiver},#{flags}"
  end
end

log_file = ARGV[0]
extract_message_info(log_file)

#File.foreach(log_file) do |line|
