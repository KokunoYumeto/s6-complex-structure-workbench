"""Exploratory log-height spectrum of the EXACT census; not a spectral certificate."""
import numpy as np
from scipy.signal import find_peaks
from pathlib import Path
path=Path(__file__).resolve().parent
h=np.fromfile(path/'A_census_1e9.u32',dtype='<u4')
C=9*np.log(2+np.sqrt(3))*np.log(3/(2*np.sqrt(2)))/(2*np.pi**2)
N=32768
r=np.linspace(np.log(1e4),np.log(1e9),N,endpoint=False)
x=np.exp(r)
y=(np.searchsorted(h,x,side='right')-C*x)/np.sqrt(x)
win=np.hanning(N)
# A zero-padded DFT resolves peak location visually; resolution remains 2*pi/log(1e5).
freq=np.fft.rfftfreq(16*N,d=(r[1]-r[0]))*2*np.pi
amp=np.abs(np.fft.rfft((y-np.average(y,weights=win))*win,n=16*N))*2/win.sum()
peaks,_=find_peaks(amp)
peaks=sorted([p for p in peaks if .5<freq[p]<100],key=lambda p:amp[p],reverse=True)[:16]
print('Exploratory only: windowed finite log-height DFT, no certified eigenvalue or nonvanishing inference.')
print('X range [1e4,1e9], N=',N,'raw resolution=',2*np.pi/np.log(1e5))
for p in peaks:print(f't={freq[p]:.8f}, windowed amplitude={amp[p]:.10f}')
np.savetxt(path/'A_log_spectrum.csv',np.c_[freq[freq<=100],amp[freq<=100]],delimiter=',',header='log_frequency,windowed_amplitude',comments='')
