if model.HttpMethod == 'get':
    html = model.Content("FPUPacketForm.html")
    model.Form = model.RenderTemplate(html)
    model.Script = model.Content("FPUPacket.js")

elif model.HttpMethod == 'post':
    print model.CallScript('FPUPacketProcess.py')

