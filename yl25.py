thisdict = {
    'eesnimi':'Ken-Martti',
    'perenimi':'Paju',
    'sünniaasta':'2007',
    'elukoht':'Saaremaa',
    'Lemmik toit':'Snitsel'
}

thisdict['Lemmik toit'] = 'muna'

print(thisdict['elukoht'])

x = thisdict.get('elukoht')

print(x)

print(len(thisdict))

thisdict.pop('sünniaasta')

thisdict['pikkus'] = 188

print(thisdict)