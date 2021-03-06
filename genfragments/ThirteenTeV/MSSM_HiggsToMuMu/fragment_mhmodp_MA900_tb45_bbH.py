COM_ENERGY = 13000.0 # GeV
CROSS_SECTION = 1 # pb
PROCESS = 'HiggsBSM:gg2H2bbbar = on'
SLHA_TABLE = """BLOCK SPINFO
     1   FeynHiggs
     2   2.12.0
     2   built on ott 13, 2016
BLOCK MODSEL
         1                  0   # Model
         2                  1   # GridPts
         3                  0   # Content
         4                  0   # RPV
         5                  0   # CPV
         6                  0   # FV
BLOCK SMINPUTS
         1     1.28952828E+02   # invAlfaMZ
         2     1.16637000E-05   # GF
         3     1.19000000E-01   # AlfasMZ
         4     9.11876000E+01   # MZ
         5     4.16000000E+00   # Mb
         6     1.73200000E+02   # Mt
         7     1.77703000E+00   # Mtau
        11     5.10998902E-04   # Me
        13     1.05658357E-01   # Mmu
        21     6.00000000E-03   # Md
        22     3.00000000E-03   # Mu
        23     9.50000000E-02   # Ms
        24     1.28600000E+00   # Mc
BLOCK MINPAR
         3     4.50000000E+01   # TB
BLOCK EXTPAR
         0     0.00000000E+00   # Q
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        11     1.50444444E+03   # At
        12     1.50444444E+03   # Ab
        13     1.50444444E+03   # Atau
        23     2.00000000E+02   # MUE
        25     4.50000000E+01   # TB
        26     9.00000000E+02   # MA0
        27     9.03583886E+02   # MHp
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK MASS
   1000012     4.95829119E+02   # MSf(1,1,1)
   1000011     5.02298735E+02   # MSf(1,2,1)
   2000011     5.01846058E+02   # MSf(2,2,1)
   1000002     1.49902619E+03   # MSf(1,3,1)
   2000002     1.49958894E+03   # MSf(2,3,1)
   1000001     1.50117883E+03   # MSf(1,4,1)
   2000001     1.50020518E+03   # MSf(2,4,1)
   1000014     4.95829119E+02   # MSf(1,1,2)
   1000013     5.03045178E+02   # MSf(1,2,2)
   2000013     5.01097851E+02   # MSf(2,2,2)
   1000004     1.49902674E+03   # MSf(1,3,2)
   2000004     1.49958950E+03   # MSf(2,3,2)
   1000003     1.50124953E+03   # MSf(1,4,2)
   2000003     1.50013444E+03   # MSf(2,4,2)
   1000016     9.97921097E+02   # MSf(1,1,3)
   1000015     9.94363181E+02   # MSf(1,2,3)
   2000015     1.00767141E+03   # MSf(2,2,3)
   1000006     8.76424627E+02   # MSf(1,3,3)
   2000006     1.13477877E+03   # MSf(2,3,3)
   1000005     9.87305500E+02   # MSf(1,4,3)
   2000005     1.01459737E+03   # MSf(2,4,3)
        25     1.25228765E+02   # Mh0
        35     8.99496414E+02   # MHH
        36     9.00000000E+02   # MA0
        37     9.03820593E+02   # MHp
   1000022     8.86520875E+01   # MNeu(1)
   1000023     1.52522347E+02   # MNeu(2)
   1000025    -2.10705170E+02   # MNeu(3)
   1000035     2.65002387E+02   # MNeu(4)
   1000024     1.49478373E+02   # MCha(1)
   1000037     2.65676293E+02   # MCha(2)
   1000021     1.50000000E+03   # MGl
BLOCK DMASS
         0     1.73200000E+02   # Q
        25     7.19171038E-01   # Delta Mh0
        35     6.68038409E-02   # Delta MHH
        36     0.00000000E+00   # Delta MA0
        37     4.75809603E-02   # Delta MHp
BLOCK NMIX
     1   1     9.35098280E-01   # ZNeu(1,1)
     1   2    -1.07012366E-01   # ZNeu(1,2)
     1   3     3.06819526E-01   # ZNeu(1,3)
     1   4    -1.41426089E-01   # ZNeu(1,4)
     2   1    -3.08703658E-01   # ZNeu(2,1)
     2   2    -6.93131494E-01   # ZNeu(2,2)
     2   3     5.15654421E-01   # ZNeu(2,3)
     2   4    -3.97958919E-01   # ZNeu(2,4)
     3   1     9.84352273E-02   # ZNeu(3,1)
     3   2    -1.37118118E-01   # ZNeu(3,2)
     3   3    -6.77717093E-01   # ZNeu(3,3)
     3   4    -7.15687550E-01   # ZNeu(3,4)
     4   1    -1.43540113E-01   # ZNeu(4,1)
     4   2     6.99511048E-01   # ZNeu(4,2)
     4   3     4.25043337E-01   # ZNeu(4,3)
     4   4    -5.56254160E-01   # ZNeu(4,4)
BLOCK UMIX
     1   1    -6.05094408E-01   # UCha(1,1)
     1   2     7.96153728E-01   # UCha(1,2)
     2   1     7.96153728E-01   # UCha(2,1)
     2   2     6.05094408E-01   # UCha(2,2)
BLOCK VMIX
     1   1    -7.96153728E-01   # VCha(1,1)
     1   2     6.05094408E-01   # VCha(1,2)
     2   1     6.05094408E-01   # VCha(2,1)
     2   2     7.96153728E-01   # VCha(2,2)
BLOCK STAUMIX
     1   1     7.01050264E-01   # USf(1,1)
     1   2     7.13111862E-01   # USf(1,2)
     2   1     7.13111862E-01   # USf(2,1)
     2   2    -7.01050264E-01   # USf(2,2)
BLOCK STOPMIX
     1   1     7.08254055E-01   # USf(1,1)
     1   2    -7.05957643E-01   # USf(1,2)
     2   1     7.05957643E-01   # USf(2,1)
     2   2     7.08254055E-01   # USf(2,2)
BLOCK SBOTMIX
     1   1     6.87948523E-01   # USf(1,1)
     1   2     7.25759484E-01   # USf(1,2)
     2   1     7.25759484E-01   # USf(2,1)
     2   2    -6.87948523E-01   # USf(2,2)
BLOCK ALPHA
              -2.30827963E-02   # Alpha
BLOCK DALPHA
               1.34158705E-05   # Delta Alpha
BLOCK HMIX Q= -0.99900000E+03
         1     2.00000000E+02   # MUE
         2     4.50000000E+01   # TB
BLOCK MSOFT Q=  0.00000000E+00
         1     9.54716519E+01   # M1
         2     2.00000000E+02   # M2
         3     1.50000000E+03   # M3
        31     5.00000000E+02   # MSL(1)
        32     5.00000000E+02   # MSL(2)
        33     1.00000000E+03   # MSL(3)
        34     5.00000000E+02   # MSE(1)
        35     5.00000000E+02   # MSE(2)
        36     1.00000000E+03   # MSE(3)
        41     1.50000000E+03   # MSQ(1)
        42     1.50000000E+03   # MSQ(2)
        43     1.00000000E+03   # MSQ(3)
        44     1.50000000E+03   # MSU(1)
        45     1.50000000E+03   # MSU(2)
        46     1.00000000E+03   # MSU(3)
        47     1.50000000E+03   # MSD(1)
        48     1.50000000E+03   # MSD(2)
        49     1.00000000E+03   # MSD(3)
BLOCK AE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50444444E+03   # Af(3,3)
BLOCK AU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50444444E+03   # Af(3,3)
BLOCK AD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Af(1,1)
     2   2     0.00000000E+00   # Af(2,2)
     3   3     1.50444444E+03   # Af(3,3)
BLOCK YE Q=  0.00000000E+00
     1   1     1.32108376E-04   # Yf(1,1)
     2   2     2.73158199E-02   # Yf(2,2)
     3   3     4.59414975E-01   # Yf(3,3)
BLOCK YU Q=  0.00000000E+00
     1   1     1.72353112E-05   # Yf(1,1)
     2   2     7.38820339E-03   # Yf(2,2)
     3   3     9.95051965E-01   # Yf(3,3)
BLOCK YD Q=  0.00000000E+00
     1   1     1.48292273E-03   # Yf(1,1)
     2   2     2.34774081E-02   # Yf(2,2)
     3   3     9.40874147E-01   # Yf(3,3)
BLOCK VCKMIN
         1     2.25300000E-01   # lambda
         2     8.08000000E-01   # A
         3     1.32000000E-01   # rhobar
         4     3.41000000E-01   # etabar
BLOCK MSL2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSL2(1,1)
     2   2     2.50000000E+05   # MSL2(2,2)
     3   3     1.00000000E+06   # MSL2(3,3)
BLOCK MSE2 Q=  0.00000000E+00
     1   1     2.50000000E+05   # MSE2(1,1)
     2   2     2.50000000E+05   # MSE2(2,2)
     3   3     1.00000000E+06   # MSE2(3,3)
BLOCK MSQ2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSQ2(1,1)
     2   2     2.25000000E+06   # MSQ2(2,2)
     3   3     1.00000000E+06   # MSQ2(3,3)
BLOCK MSU2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSU2(1,1)
     2   2     2.25000000E+06   # MSU2(2,2)
     3   3     1.00000000E+06   # MSU2(3,3)
BLOCK MSD2 Q=  0.00000000E+00
     1   1     2.25000000E+06   # MSD2(1,1)
     2   2     2.25000000E+06   # MSD2(2,2)
     3   3     1.00000000E+06   # MSD2(3,3)
BLOCK TE Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     6.91164307E+02   # Tf(3,3)
BLOCK TU Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.49700040E+03   # Tf(3,3)
BLOCK TD Q=  0.00000000E+00
     1   1     0.00000000E+00   # Tf(1,1)
     2   2     0.00000000E+00   # Tf(2,2)
     3   3     1.41549288E+03   # Tf(3,3)
BLOCK SELMIX
     1   1     9.99948810E-01   # UASf(1,1)
     1   4    -1.01181234E-02   # UASf(1,4)
     2   2     7.84988373E-01   # UASf(2,2)
     2   5    -6.19510496E-01   # UASf(2,5)
     3   3     7.01050264E-01   # UASf(3,3)
     3   6     7.13111862E-01   # UASf(3,6)
     4   1     1.01181234E-02   # UASf(4,1)
     4   4     9.99948810E-01   # UASf(4,4)
     5   2     6.19510496E-01   # UASf(5,2)
     5   5     7.84988373E-01   # UASf(5,5)
     6   3     7.13111862E-01   # UASf(6,3)
     6   6    -7.01050264E-01   # UASf(6,6)
BLOCK USQMIX
     1   1     1.00000000E+00   # UASf(1,1)
     1   4     7.90138244E-06   # UASf(1,4)
     2   2     9.99994264E-01   # UASf(2,2)
     2   5     3.38700099E-03   # UASf(2,5)
     3   3     7.08254055E-01   # UASf(3,3)
     3   6    -7.05957643E-01   # UASf(3,6)
     4   1    -7.90138244E-06   # UASf(4,1)
     4   4     1.00000000E+00   # UASf(4,4)
     5   2    -3.38700099E-03   # UASf(5,2)
     5   5     9.99994264E-01   # UASf(5,5)
     6   3     7.05957643E-01   # UASf(6,3)
     6   6     7.08254055E-01   # UASf(6,6)
BLOCK DSQMIX
     1   1     9.99843904E-01   # UASf(1,1)
     1   4    -1.76682471E-02   # UASf(1,4)
     2   2     9.67630109E-01   # UASf(2,2)
     2   5    -2.52372687E-01   # UASf(2,5)
     3   3     6.87948523E-01   # UASf(3,3)
     3   6     7.25759484E-01   # UASf(3,6)
     4   1     1.76682471E-02   # UASf(4,1)
     4   4     9.99843904E-01   # UASf(4,4)
     5   2     2.52372687E-01   # UASf(5,2)
     5   5     9.67630109E-01   # UASf(5,5)
     6   3     7.25759484E-01   # UASf(6,3)
     6   6    -6.87948523E-01   # UASf(6,6)
BLOCK CVHMIX
     1   1     9.99999918E-01   # UH(1,1)
     1   2     4.03948776E-04   # UH(1,2)
     1   3     0.00000000E+00   # UH(1,3)
     2   1    -4.03948776E-04   # UH(2,1)
     2   2     9.99999918E-01   # UH(2,2)
     2   3     0.00000000E+00   # UH(2,3)
     3   1     0.00000000E+00   # UH(3,1)
     3   2     0.00000000E+00   # UH(3,2)
     3   3     1.00000000E+00   # UH(3,3)
DECAY        25     4.01829006E-03   # Gamma(h0)
     2.30114595E-03   2        22        22   # BR(h0 -> photon photon)
     1.49253777E-03   2        22        23   # BR(h0 -> photon Z)
     2.74751883E-02   2        23        23   # BR(h0 -> Z Z)
     2.25942049E-01   2       -24        24   # BR(h0 -> W W)
     7.07335458E-02   2        21        21   # BR(h0 -> gluon gluon)
     5.37272818E-09   2       -11        11   # BR(h0 -> Electron electron)
     2.38988386E-04   2       -13        13   # BR(h0 -> Muon muon)
     6.85087226E-02   2       -15        15   # BR(h0 -> Tau tau)
     2.00936016E-07   2        -2         2   # BR(h0 -> Up up)
     2.78318417E-02   2        -4         4   # BR(h0 -> Charm charm)
     8.75029314E-07   2        -1         1   # BR(h0 -> Down down)
     2.19747042E-04   2        -3         3   # BR(h0 -> Strange strange)
     5.75255152E-01   2        -5         5   # BR(h0 -> Bottom bottom)
DECAY        35     3.11871157E+01   # Gamma(HH)
    -1.53363319E-07   2        22        22   # BR(HH -> photon photon)
    -6.78747833E-07   2        22        23   # BR(HH -> photon Z)
    -3.47043786E-06   2        23        23   # BR(HH -> Z Z)
    -5.20853453E-06   2       -24        24   # BR(HH -> W W)
    -4.00541929E-05   2        21        21   # BR(HH -> gluon gluon)
    -9.73470474E-09   2       -11        11   # BR(HH -> Electron electron)
     4.33274782E-04   2       -13        13   # BR(HH -> Muon muon)
    -1.19788017E-01   2       -15        15   # BR(HH -> Tau tau)
    -5.67346257E-14   2        -2         2   # BR(HH -> Up up)
    -7.85233873E-09   2        -4         4   # BR(HH -> Charm charm)
    -4.08249453E-04   2        -6         6   # BR(HH -> Top top)
    -9.97493338E-07   2        -1         1   # BR(HH -> Down down)
    -2.50482624E-04   2        -3         3   # BR(HH -> Strange strange)
    -5.63950861E-01   2        -5         5   # BR(HH -> Bottom bottom)
    -7.75096726E-02   2  -1000024   1000024   # BR(HH -> Chargino1 chargino1)
    -4.96326760E-02   2  -1000037   1000024   # BR(HH -> Chargino2 chargino1)
    -4.96326760E-02   2  -1000024   1000037   # BR(HH -> Chargino1 chargino2)
    -1.53308474E-02   2  -1000037   1000037   # BR(HH -> Chargino2 chargino2)
    -7.56780822E-03   2   1000022   1000022   # BR(HH -> neutralino1 neutralino1)
    -2.30609970E-02   2   1000022   1000023   # BR(HH -> neutralino1 neutralino2)
    -1.43586313E-02   2   1000022   1000025   # BR(HH -> neutralino1 neutralino3)
    -1.95468802E-05   2   1000022   1000035   # BR(HH -> neutralino1 neutralino4)
    -1.40582461E-02   2   1000023   1000023   # BR(HH -> neutralino2 neutralino2)
    -7.84886999E-03   2   1000023   1000025   # BR(HH -> neutralino2 neutralino3)
    -2.51007073E-03   2   1000023   1000035   # BR(HH -> neutralino2 neutralino4)
    -2.82785596E-03   2   1000025   1000025   # BR(HH -> neutralino3 neutralino3)
    -3.79733602E-02   2   1000025   1000035   # BR(HH -> neutralino3 neutralino4)
    -1.27579428E-02   2   1000035   1000035   # BR(HH -> neutralino4 neutralino4)
    -2.93330776E-05   2        25        25   # BR(HH -> h0 h0)
DECAY        36     3.06296969E+01   # Gamma(A0)
     4.89120994E-07   2        22        22   # BR(A0 -> photon photon)
     9.68971009E-07   2        22        23   # BR(A0 -> photon Z)
     6.04490119E-05   2        21        21   # BR(A0 -> gluon gluon)
     9.65254369E-09   2       -11        11   # BR(A0 -> Electron electron)
     4.29618176E-04   2       -13        13   # BR(A0 -> Muon muon)
     1.18778591E-01   2       -15        15   # BR(A0 -> Tau tau)
     5.26672868E-14   2        -2         2   # BR(A0 -> Up up)
     7.29058403E-09   2        -4         4   # BR(A0 -> Charm charm)
     4.47442324E-04   2        -6         6   # BR(A0 -> Top top)
     9.88997835E-07   2        -1         1   # BR(A0 -> Down down)
     2.48349339E-04   2        -3         3   # BR(A0 -> Strange strange)
     5.59187698E-01   2        -5         5   # BR(A0 -> Bottom bottom)
     9.35523097E-02   2  -1000024   1000024   # BR(A0 -> Chargino1 chargino1)
     3.69818828E-02   2  -1000037   1000024   # BR(A0 -> Chargino2 chargino1)
     3.69818828E-02   2  -1000024   1000037   # BR(A0 -> Chargino1 chargino2)
     2.80797977E-02   2  -1000037   1000037   # BR(A0 -> Chargino2 chargino2)
     8.36426840E-03   2   1000022   1000022   # BR(A0 -> neutralino1 neutralino1)
     2.67553601E-02   2   1000022   1000023   # BR(A0 -> neutralino1 neutralino2)
     1.17763005E-02   2   1000022   1000025   # BR(A0 -> neutralino1 neutralino3)
     6.55778677E-05   2   1000022   1000035   # BR(A0 -> neutralino1 neutralino4)
     1.73580773E-02   2   1000023   1000023   # BR(A0 -> neutralino2 neutralino2)
     5.74017857E-03   2   1000023   1000025   # BR(A0 -> neutralino2 neutralino3)
     3.23457461E-03   2   1000023   1000035   # BR(A0 -> neutralino2 neutralino4)
     3.35497974E-03   2   1000025   1000025   # BR(A0 -> neutralino3 neutralino3)
     2.61684363E-02   2   1000025   1000035   # BR(A0 -> neutralino3 neutralino4)
     2.24264383E-02   2   1000035   1000035   # BR(A0 -> neutralino4 neutralino4)
     5.32344107E-06   2        23        25   # BR(A0 -> Z h0)
     1.78675113E-36   2        25        25   # BR(A0 -> h0 h0)
DECAY        37     2.96398612E+01   # Gamma(Hp)
     1.02197742E-08   2       -11        12   # BR(Hp -> Electron nu_e)
     4.36927178E-04   2       -13        14   # BR(Hp -> Muon nu_mu)
     1.23591194E-01   2       -15        16   # BR(Hp -> Tau nu_tau)
     9.89154759E-07   2        -1         2   # BR(Hp -> Down up)
     1.14113316E-05   2        -3         2   # BR(Hp -> Strange up)
     6.09296468E-06   2        -5         2   # BR(Hp -> Bottom up)
     4.58843579E-08   2        -1         4   # BR(Hp -> Down charm)
     2.47517088E-04   2        -3         4   # BR(Hp -> Strange charm)
     8.53229913E-04   2        -5         4   # BR(Hp -> Bottom charm)
     4.22249771E-08   2        -1         6   # BR(Hp -> Down top)
     1.25715840E-06   2        -3         6   # BR(Hp -> Strange top)
     5.46482589E-01   2        -5         6   # BR(Hp -> Bottom top)
     3.84199853E-02   2   1000022   1000024   # BR(Hp -> neutralino1 chargino1)
     1.17037529E-03   2   1000022   1000037   # BR(Hp -> neutralino1 chargino2)
     6.51889906E-03   2   1000023   1000024   # BR(Hp -> neutralino2 chargino1)
     1.18212721E-01   2   1000023   1000037   # BR(Hp -> neutralino2 chargino2)
     4.41669986E-02   2   1000024   1000025   # BR(Hp -> chargino1 neutralino3)
     4.64663255E-02   2   1000025   1000037   # BR(Hp -> neutralino3 chargino2)
     7.25426761E-02   2   1000024   1000035   # BR(Hp -> chargino1 neutralino4)
     8.65096688E-04   2   1000035   1000037   # BR(Hp -> neutralino4 chargino2)
     5.61673820E-06   2        24        25   # BR(Hp -> W h0)
     6.90570954E-11   2        24        35   # BR(Hp -> W HH)
     3.72006701E-11   2        24        36   # BR(Hp -> W A0)
DECAY         6     1.37127534E+00   # Gamma(top)
     1.00000000E+00   2         5        24   # BR(top -> bottom W)
"""

import FWCore.ParameterSet.Config as cms

from Configuration.Generator.Pythia8CommonSettings_cfi import *
from Configuration.Generator.Pythia8CUEP8M1Settings_cfi import *

generator = cms.EDFilter("Pythia8GeneratorFilter",
                         pythiaPylistVerbosity = cms.untracked.int32(1),                        
                         filterEfficiency = cms.untracked.double(1),
                         pythiaHepMCVerbosity = cms.untracked.bool(False),
                         SLHATableForPythia8 = cms.string('%s' % SLHA_TABLE),
                         comEnergy = cms.double(COM_ENERGY),
                         crossSection = cms.untracked.double(CROSS_SECTION),                         
                         maxEventsToPrint = cms.untracked.int32(1),
                         PythiaParameters = cms.PSet(
                             pythia8CommonSettingsBlock,
                             pythia8CUEP8M1SettingsBlock,
                             processParameters = cms.vstring(
                                 'Higgs:useBSM = on', 
                                 PROCESS, 
                                 'SLHA:allowUserOverride = off', 
                                 'SLHA:minMassSM = 100.', 
                                 'PhaseSpace:mHatMin = 56.0'
                             ),
                             parameterSets = cms.vstring(
                                 'pythia8CommonSettings',
                                 'pythia8CUEP8M1Settings',
                                 'processParameters'
                                 )
                             )
                         )

ProductionFilterSequence = cms.Sequence(generator)
