from CEAfunctions import engine,writefile,runcea,readcea
import subprocess
AresEngine = engine('300','psi','27.2','CH4','O2(L)','2.0','298','90.17')
writefile(AresEngine)
runcea()
runcea()
readcea()
