var.chords = var([0,3], 8)

p1 >> ambi(P[var.chords,4,6,7][:6], dur=PDur(3,8)*2, amp=0.2, sus=2, blur=1, oct=4)

p1.stop()


v1 >> viola([7,6,4,2, b2.pitch, var.chords] + var([0,2], 8), dur=[2,2,2,8], oct=6, blur=1.5, amp=0.1).every(8, 'shuffle')

v1.stop()


p3 >> piano(P[var.chords, 1, 5, 8][:6], dur=1, sus=4, blur=1.5, amp=[0.2]).every([4,2], 'shuffle')
p3.rate=PWhite(5,10)

p3.stop()



cm >> klank(var.chords + [-5,2,1], sus=6, amp=0.1).offbeat()
cm.rate=PWhite(10,70)


lm >> soprano(cm + [15,-11,-22], sus=4, amp=0.1)
lm.rate=PWhite(30,50)

Group(lm, cm).stop()


s1 >> klank(PSine(15), oct=1, pan=[-1,0,1], amp=1)
p2 >> ambi(PSine(1), oct=2, amp=1)

Group(s1,p2).stop()


d1 >> play('x - o - [xx] - o - ', sample=6, amp=0.8, pan=(-1,1))
c1 >> crunch(dur=1)

d1.stop()

d2 >> play('<x[ [n]] >< h>', dur=1, sample=6, amp=0.3)

d3 >> play("x -- \f- o x- [x] trv \f", amp=0.3, sample=4 ,rate=PWhite(5,10), pan=[1,-1]).every([3,8], 'shuffle')

d3.stop()

hh >> play("  ( sH) ", amp=0.3, sample=4)
cc >> play("m  m  m ", amp=0.25)

Group(hh, cc).stop()


d4 >> play("x x x -o", amp=0.3, pan=[1,0,-1])

d4.stop()

d5 >> play("t\fr[\\f]-t --x   v \f", amp=0.3)
d5.rate=PWhite(10,50)

d5.stop()

d_all.solo()

d_all.amp = 0

d_all.stop()
