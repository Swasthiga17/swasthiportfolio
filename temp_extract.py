import re

with open(r'c:\Users\lenovo\portfolio\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Find rotating roles JS
idx = content.find('const roles')
if idx >= 0:
    print("=== ROTATING ROLES ===")
    print(content[idx:idx+400])
else:
    print("ROTATING ROLES: NOT FOUND")

# 2. Check for resume section
idx2 = content.find('id="resume"')
if idx2 >= 0:
    print("\n=== RESUME SECTION ===")
    print(content[idx2:idx2+600])
else:
    print("\nRESUME SECTION: NOT FOUND")

# 3. Check contact section
idx3 = content.find('id="contact"')
if idx3 >= 0:
    print("\n=== CONTACT SECTION ===")
    print(content[idx3:idx3+800])
else:
    print("\nCONTACT SECTION: NOT FOUND")

# 4. About text
idx4 = content.find('about-text')
if idx4 >= 0:
    print("\n=== ABOUT TEXT ===")
    print(content[max(0,idx4-100):idx4+600])
else:
    print("\nABOUT TEXT: NOT FOUND")

# 5. Stat boxes
idx5 = content.find('stat-box')
if idx5 >= 0:
    print("\n=== STAT BOXES ===")
    print(content[max(0,idx5-200):idx5+600])
else:
    print("\nSTAT BOXES: NONE FOUND")

# 6. Hero photo badge
idx6 = content.find('hero-photo-badge')
if idx6 >= 0:
    print("\n=== HERO PHOTO BADGE ===")
    print(content[idx6:idx6+300])
else:
    print("\nHERO PHOTO BADGE: NOT FOUND")

# 7. Check hire-banner
idx7 = content.find('hire-banner')
if idx7 >= 0:
    print("\n=== HIRE BANNER ===")
    print(content[max(0,idx7-50):idx7+300])
else:
    print("\nHIRE BANNER: NOT FOUND (needs to be added)")

print("\n=== FILE LENGTH ===")
print(f"Total chars: {len(content)}")
print(f"Lines: {content.count(chr(10))}")
