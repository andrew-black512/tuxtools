#!/usr/bin/ruby
require 'fileutils'

# TODO
#   - tidy glob (eg .TXT - *.TXT)
#   - allow different formats

def createdir (dirname)
    if ! Dir.exist?(dirname)
        puts "create #{dirname}"
        FileUtils.mkdir_p(dirname) 
    end

end


#---------------------------------------------------------------------------
def helpandexit
    puts <<HELP 
    
    zoneify.rb  filemask [format]
        (remember to quote regep)
        
HELP
    exit
end
#---------------------------------------------------------------------------
formats = {
    'ymd' =>  '%Y_%m_%d' ,
    'yw'  =>  '%Y_w%V'   ,
}
#---------------------------------------------------------------------------

helpandexit if ARGV.count == 0 
fileglob = ARGV.shift

format = ARGV.count == 1 ? ARGV.shift  :   '%Y_%m_%d'

Dir.glob(fileglob).each do |filename|
    if File.file?(filename)       # not directory
        f=File.new filename
        dirname = f.mtime.strftime( format )  # _%d configurable?s
        createdir dirname

        puts "  Move #{filename} to #{dirname}" 
        # FileUtils.mv( filename, dirname + '/' )
    end 
end
