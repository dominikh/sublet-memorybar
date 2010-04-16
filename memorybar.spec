# -*- encoding: utf-8 -*-
# memorybar specification file
# Created with sur-0.2.155
Sur::Specification.new do |s|
  s.name        = "memorybar"
  s.authors     = [ "Dominik Honnef" ]
  s.date        = "Sun Apr 11 15:28 CEST 2010"
  s.contact     = "dominikho@gmx.net"
  s.description = "Shows memory usage using a bar"
  s.version     = "0.1"
  s.tags        = [ "memory", "bar" ]
  s.files       = [ "memorybar.rb" ]
  s.icons       = [ ]
  s.add_dependency "subtle-graph", "0.0.2"
  s.subtlext_version = "0.9.1883"
end
