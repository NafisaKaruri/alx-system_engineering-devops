#!/usr/bin/env ruby
puts ARGV[0].scan(/\s\[from:(.*?)\]\s\[to:(.*?)\]?\s\[flags:(.*?)\]/).join(',')
