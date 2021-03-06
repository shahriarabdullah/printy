from .core import Printy

helpme = """#########################################################
#########################################################

[bBH]PRINTY@

Printy lets you colorize and apply some standard formats to your text with
an intuitive and friendly API based on flags to specify the formats. You can
either apply a global format or inline formats to specific parts of your text!
And yes, this whole tutorial is written with Printy!!

[gI]NOTE: If you are on windows, you may not see some of the formats due
to Windows console limitations@

[n]Let's get started!@

[B]COLORS@

[g]'g' -> Applies a grey color to the text@
[r]'r' -> Applies a red color to the text@
[n]'n' -> Applies a green color to the text@
[y]'y' -> Applies a yellow color to the text@
[b]'b' -> Applies a blue color to the text@
[m]'m' -> Applies a magenta color to the text@
[c]'c' -> Applies a cyan color to the text@
[k]'k' -> Applies a black color to the text@
[w]'w' -> Applies a white color to the text@
[p]'p' -> Applies the predefined color to the text@

[B]FORMATS@

[B]'B' -> Applies a bold font weight to the text@
[D]'D' -> Decrease the intensity, aka Dim@
[U]'U' -> Applies an underline to the text@
[I]'I' -> Applies an italic font type to the text@
[H]'H' -> Highlights the text@
[S]'S' -> crosses out the text, aka Strike@


[B]HOW TO USE IT?@

First import printy:

[n]    >>>@ [r]from@ printy [r]import@ printy

Now apply one or more of the available flags to the text like this:

[n]    >>>@ printy([c]'Some text to be formatted'@[r],@ [c]'b'@)
    [b]Some text to be formatted@

[n]    >>>@ printy([c]'Some text to be formatted'@[r],@ [c]'bHI'@)
    [bHI]Some text to be formatted@

Or as Inline format, use the \[\] to specify the flags, and the \@ to finish
the format for a specific section:

[n]    >>>@ printy([c]'\[r\]Red\@ Default Color \[yH\]Yellow Highlighted\@ Default Color'@)
    [r]Red@ Default Color [yH]Yellow Highlighted@ Default Color

You can always override the whole format with a global flag:

[n]    >>>@ printy([c]'\[r\]Red\@ Default Color \[yH\]Yellow Highlighted\@ Default Color'@[r],@ [c]'b'@)
    [b]Red Default Color Yellow Highlighted Default Color@

Or you can change only the default color:

[n]    >>>@ printy([c]'\[r\]Red\@ Default Color \[yH\]Yellow Highlighted\@ Default Color'@[r], default@=[c]'b'@)
    [r]Red@ [b]Default Color@ [yH]Yellow Highlighted@ [b]Default Color@

[n]    >>>@ printy([c]'\[r\]Red\@ Default Color \[yH\]Yellow Highlighted\@ Default Color'@[r], default@=[c]'nBIU'@)
    [r]Red@ [nBIU]Default Color@ [yH]Yellow Highlighted@ [nBIU]Default Color@

If you need to use one of the special characters ('\[', '\]', '\@'), simply escape them ensure
they show up, or, in case they are not placed in the form '\[flags\]Text\@'), you can include
them without escaping, the algorithm will treat them as regular characters:

[n]    >>>@ printy([c]'\[B\]\\\[myemail\\\@mydomain.com\\\]\@'@)
    [B]\[myemail\@mydomain.com\]@

[n]    >>>@ [g]# Here, the emails's '\@' would close the '\[B\]' statement,@
[n]    >>>@ [g]# so we need to escape it anyway. But look at how we don't @
[n]    >>>@ [g]# escape the \[ and \] characters. @
[n]    >>>@ printy([c]'\[B\]\[myemail\\\@mydomain.com\]\@'@)
    [B][myemail\@mydomain.com]@

Now you can do stuffs like:

[n]    >>>@ text = 'Hello world, python is awesome!!!'
[n]    >>>@ printy(text.replace([c]'python'@[r],@ [c]'\[r\]python\@'@))
    Hello world, [r]python@ is awesome

Or some html highlighting:

[n]    >>>@ html = (
[n]    ...@ [c]'<div \[p\]class=\@\[n\]"active"\@ \[p\]id=\@\[n\]"my-div"\@>'@
[n]    ...@ [c]'    <span \[p\]data-some-data=\@\[n\]"extra-data"\@>\[p\]Some text\@</span>'@
[n]    ...@ [c]'</div>'@)
[n]    >>>@ printy(html[r], default@=[c]'r'@)
    [r]<div@ class=[n]'active'@ id=[n]'my-div'@[r]>@
        [r]<span@ data-some-data=[n]'extra-data'@[r]>@Some text[r]</span>@
    [r]</div>@

Or, you can use it with python's formatting strings as well:

[n]    >>>@ minutes = [b]60@
[n]    >>>@ printy([c]f'A day has \[y\]@[r]{@[p]minutes * @[b]24@[r]}@[c]\@ minutes'@)
    A day has [y]1400@ minutes

[B]What about @[b]input@()?

printy comes with a wrapper for the python builtins input() function

[n]    >>>@ [r]from@ printy [r]import@ inputy

Try adding adding some formats the same way you did with printy.

[By]Check this link for a full documentation!@

https://github.com/edraobdu/printy    
"""

print(Printy().get_formatted_text(helpme))

