from ircconfig import *

SETTINGS = {
    "foo": SettingString("bar")
}

p = Preferences("test.json", SETTINGS)

print(f"foo is {p.getPreference('foo')}")
p.setPreference("foo", "foobar")
print(f"foo is now {p.getPreference('foo')}")
p.setPreference("foo", "footbar", channel="#test")
print(f"foo for #test is {p.getPreference('foo', channel='#test')}")
