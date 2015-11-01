def Process():
    if '-' not in model.Data.wandtarget:
        return
    
    a = model.Data.wandtarget.split('-')
    oid = a[0]
    pid = a[1]
    
    p = model.GetPerson(pid)
    sp = model.GetSpouse(pid)
    if sp is not None:
        spid = sp.PeopleId
    o = model.GetOrganization(oid)
    inorg = model.InOrg(pid, oid)
    
    if p == None:
        print "<h3 class='alert alert-danger'>Person {0} not Found</h3>".format(pid)
    
    if o == None:
        print "<h3 class='alert alert-danger'>Organization {0} not Found</h3>".format(oid)
    
    if not inorg:
        print "<h3 class='alert alert-danger'>Person {0} not in {1}</h3>".format(pid, oid)
    
    if p is not None and o is not None:
        print '''
        <table class="table">
        <tr><td align="right">Org:</td><td><b>{0}</b></td></tr>
        <tr><td align="right">Name:</td><td><b>{1}</b></td></tr>
        '''.format(o.name, p.Name)
    
        if not inorg:
            print '</table>'
            return
    
        if sp is not None and model.InOrg(spid, oid):
            print '''
            <tr><td align="right">Spouse:</td><td><b>{0}</b></td></tr>
            '''.format(sp.Name)
    
        print '</table>'
    
        if model.Data.paidoption == "markpaid":
            model.AddSubGroup(pid, oid, "pay online")
            print "<h3 class='alert alert-warning'>Marked Now As Paid</h3>"
        elif model.Data.paidoption == "marknotpaid":
            model.RemoveSubGroup(pid, oid, "pay online")
            print "<h3 class='alert alert-warning'>Marked Now As Not Paid</h3>"
        else:
            if model.InSubGroup(pid, oid, "pay online"):
                print "<h3 class='alert alert-success'>Packet Paid For Already</h3>"
            elif sp is not None and model.InSubGroup(spid, oid, "pay online"):
                print "<h3 class='alert alert-success'>Packet Paid For by Spouse Already</h3>"
            else:
                print "<h3 class='alert alert-danger'>Packet Not Paid For</h3>"
    
        if model.Data.pickedup == "notpickedup":
            model.RemoveSubGroup(pid, oid, "packet-picked-up")
            print "<h3 class='alert alert-warning'>Packet Now Marked As Not Picked Up</h3>"
        else:
            if model.InSubGroup(pid, oid, "packet-picked-up"):
                print "<h3 class='alert alert-danger'>Packet Already Picked Up</h3>"
            elif sp is not None and model.InSubGroup(spid, oid, "packet-picked-up"):
                print "<h3 class='alert alert-danger'>Packet Picked Up by Spouse Already</h3>"
            else:
                model.AddSubGroup(pid, oid, "packet-picked-up")
                print "<h3 class='alert alert-success'>Packet Now Marked as Picked Up</h3>"

Process()
