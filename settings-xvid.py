#PY  <- Needed to identify #
#--automatically built--

adm = Avidemux()
adm.videoCodec("xvid4", "params=2PASSBITRATE=3500", "profile=244", "rdMode=3", "motionEstimation=3", "cqmMode=0", "arMode=1", "maxBFrame=2", "maxKeyFrameInterval=200", "nbThreads=99", "qMin=2", "qMax=25", "rdOnBFrame=True"
, "hqAcPred=True", "optimizeChrome=True", "trellis=True", "useXvidFCC=False")
adm.addVideoFilter("resampleFps", "mode=0", "newFpsDen=1000", "newFpsNum=10000")
adm.audioClearTracks()
adm.setSourceTrackLanguage(0,"unknown")
adm.audioAddTrack(0)
adm.audioCodec(0, "Lame");
adm.audioSetMixer(0, "MONO");
adm.audioSetDrc(0, 0)
adm.audioSetShift(0, 0,0)
adm.setContainer("AVI", "odmlType=1")
