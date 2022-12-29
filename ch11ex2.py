# function
#list,reverse_str=True
#list
def func(l,**kwargs):
    if kwargs.get('reverse_str')== True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]
name=['ankit','singh']
print(func(name,reverse_str=True))


def func(l,**kwargs):
    if kwargs.get('reverse_str')== True:
        return [name[::-1].title() for name in l]
    else:
        return[name.title() for name in l]
name=['ankit','singh']
print(func(name))