# Python has lots of libraries you can import
import sys

print('************************************************************************')
print(*sys.path, sep='\n')
#site_package = next(package for package in sys.path)
site_package = next(package for package in sys.path if 'site-package' in package)
#site_package = next(package for package in sys.path if 'bad' in package)
#site_package = next((package for package in sys.path if 'site-package' in package), None)

print(site_package)
