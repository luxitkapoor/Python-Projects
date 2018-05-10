import re
import pyperclip
# Phone Extracting reg ex

textInput = str(pyperclip.paste())

phoneEx = re.compile(r'''(
	(\d{3}|\(\d{3}\))?
	(\s|\.|-)?
	(\d{3})
	(\s|-|\.)
	(\d{4})
	(\s*(ext|x|ext.)\s*(\d{2,5}))?
	)''', re.VERBOSE)

# Half Working Version
# emailEx = re.compile(r'''(
# 	\w+@\w+\.\w+
# 	)''', re.VERBOSE)

emailEx = re.compile(r'''(
	[a-zA-Z0-9._%+-]+
	@
	[a-zA-Z0-9._%+-]+
	\.\w+

	)''', re.VERBOSE)


finds = []

for groups in phoneEx.findall(textInput):
    phoneNo = '-'.join([groups[1], groups[3], groups[5]])
    if groups[8] != '':
        phoneNo = phoneNo + ' x' + groups[8]
    finds.append(phoneNo)

for groups in emailEx.findall(textInput):
    finds.append(groups)

if len(finds) > 0:
    finds = '\n'.join(finds)
    pyperclip.copy(finds)
    print('Copied to clipboard')
else:
    print("No Email addresses and phone numbers found")
