kpse.set_program_name('lualatex')
local p=os.getenv('TEXMFCACHE')
print('ENV_CACHE',p)
print('KPSE_CACHE',kpse.expand_var('$TEXMFCACHE'))
local lfs=require('lfs')
print('LFS_NATIVE_WRITABLE',lfs.iswritablefile)
if lfs.iswritablefile then print('LFS_NATIVE_CACHE_RESULT',lfs.iswritablefile(p)) end
for k,v in pairs(lfs.attributes(p) or {}) do print('ATTR',k,v) end
local f,e=io.open(p..'/probe.txt','w')
print('WRITE_PROBE',f,e)
if f then f:write('probe');f:close() end
local r,e=io.open('cache/relative_probe.txt','w')
print('RELATIVE_WRITE_PROBE',r,e)
if r then r:write('probe');r:close() end
print('OPENOUT_ANY',kpse.var_value('openout_any'))
print('TEXMF_OUTPUT_DIRECTORY',os.getenv('TEXMF_OUTPUT_DIRECTORY'))
print('TEXMFOUTPUT',os.getenv('TEXMFOUTPUT'))
local ll=kpse.find_file('lualibs.lua')
print('LUALIBS',ll)
dofile(ll)
print('IS_WRITABLE',file.is_writable(p))
