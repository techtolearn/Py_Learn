'''
https://www.youtube.com/watch?v=1Xa_iDqvg94&list=PLGLfVvz_LVvTn3cK5e6LjhgGiSeVlIRwt&index=5
'''

#Ex1
# this global name is not going to change
def change_name(name):
    name = 'Tanvi'  # local var
name = "Manasvi"     # globale var
change_name('Satheesh')
print(name)
print('\n')
# this global name is going to change
def change_name(name):
    return  name # local var
name = "Manasvi"     # globale var
name = change_name('Satheesh')
print(name)
print('\n')
#Ex1 - using global var in local to change name should not implact on global name

gbl_name = "Tanvi Satheesh"
def change_name():
    global gbl_name
    gbl_name = 'Manasvi Satheesh'

change_name()
print(gbl_name)
