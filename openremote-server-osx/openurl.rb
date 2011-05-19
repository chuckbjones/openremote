#!/usr/bin/env ruby

require 'cgi'
require 'socket'


def truncate(text, length = 30, truncate_string = "...")
  if text.nil? then return end
  l = length - truncate_string.chars.to_a.size
  (text.chars.to_a.size > length ? text.chars.to_a[0...l].join + truncate_string : text).to_s
end

host = Socket.gethostname

cgi = CGI.new
url = cgi['url'] unless cgi['url'].empty?

system("open", url.untaint)

printf "Content-Type: text/plain\n\n"
printf "Opened #{truncate(url, 100)} on #{host}\n"

