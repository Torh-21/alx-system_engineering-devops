#!/usr/bin/env ruby
# This Ruby script outputs [SENDER],[RECEIVER],[FLAGS]
puts ARGV[0].scan(/\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/).join(".")
