#!/usr/bin/ruby
require "tk"

window = TkRoot.new {
   title 'gui'
#   resizable [0,0]
}
window2 = TkToplevel.new {
   title 'gui2'
    geometry '30x20+1+1'
}

#TkRoot.new() { title "Hello, Linux World ! " }
TkLabel.new(nil,:"text" => "Hello, Linux World ! ",).pack

myproc = Proc.new { puts 'a' }
name = ''
entry = TkEntry.new.pack()
#"side"=>"left"
TkButton.new{
    text 'OK'
    command myproc
    #proc{ name = entry.value;
    width 10
    height 2

    pack
}
TkButton.new(window2){
    text 'end'
    command proc { exit }
    #proc{ name = entry.value;
    width 10
    height 2

    pack 'side'=>'left', 'fill'=>'both','expand'=>'false'
}
Tk.mainloop
