piv = [1,1.5,2,2.5,3,3,4,4]
piv.extend(piv[::-1])
pivd = 16

p2 >> play(PSine(155) + PSine(15) + PSine(65))

p2.stop()

p1 >> pluck(var([9,7,3,4,2,1],8) + (0,2,0,[4,5,6]),
        dur=var(piv,pivd),
        amp=P(PRange(4,0,-1)/8 + 0.25)* 0.8,
        delay=P(PRange(4,0,-1)/4),
        formant=1, lpf=1500, hpf=200)

b3 >> bass((p1.degree - 1) + (0,2),
        dur=8, amp=0.3,
        echo=1, decay=1,
        sus=b3.dur-1.5,
        formant=(0,1))
        
Group(p1,b3).stop()

cl >> play("x -- \f o x- [x] trv \f", amp=0.6, rate=PWhite(5,10), pan=[1,-1]).every([5,10], 'shuffle')

cl.stop()

cp >> play("  ( H) ", amp=0.2)
tm >> play("m  m  m ", amp=0.1)
cd >> crunch(dur=1/4,amp=0.1)

Group(cp,tm,cd).stop()

kl >> klank(var([6,3,-5],[0,2,3]),
    dur=(piv,pivd), amp=0.2, formant=1)
    
kl.stop()

ed >> play("x   x x -o", amp=0.4, pan=[1,0,-1])

ed.stop()

sl >> soprano(piv + [0, -1, -2], sus=4, amp=0.3)

sl.stop()
