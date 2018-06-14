Clock.bpm=120

a = var([0,-2,3],[8,6,4])

kl >> klank(a + [6,3,-5], sus=5) #, pan=[-1,1])

kl.stop()

cm >> klank(a + [-5,2,1], sus=6).offbeat()
cm.rate=PWhite(10,70)


lm >> soprano(cm + [15,-11,-22], sus=4)
lm.rate=PWhite(30,50)

pl >> play(PTri(4) + PSum(6,2), scale=Scale.melodicMajor.pentatonic, oct=[6,6,7,7]).offbeat()

dd >> play('x-- o - tr v  x[ooo---] ox- x\\f', blur=3, pan=[-1,1])
dd.rate=PWhite(5,15)

cm.stop()

pl.stop()

bd >> bass(a, dur=PSum(2,7), sus=1).every([1,7], 'mirror').every([3,3], 'shuffle')

bd.stop()

lm.stop()


p1 >> pluck(P[0,2,-3,-1, 1, 5, 8], dur=1, sus=4, amp=[1,-2,-1,1]).offbeat().every([4,2], 'shuffle')
p1.rate=PWhite(5,10)

p1.pan = [-1,0,1]

p1.stop()

cd >> crunch(dur=1/4)

dd >> play("xxx  vm   ")

dd.stop()

cl >> play("t\fr[\\f]-t --x   v \f")
cl.rate=PWhite(10,50)

ed >> play("x   x  x -o", pan=[1,0,-1])



cl.stop()

ed.stop()

Group(cm, cl,dd,cd,ll,bd,pl,kl).stop()
