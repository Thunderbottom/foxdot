Scale.default.set("minor")
Root.default.set(4)



f2 >> karp (P[([0,1],8),7,6,4,2].layer("mirror"),amp=1.5, delay=(0,0.25), sus=2, dur=PDur(5,8), chop=4, oct=7).solo()
f3 >> bass(([0,[1,-1]],8), dur=PDur(5,8),amp=1,sus=0.2,oct=4, bits=1, lpf=0) + [0,4,const(7)]
f1 >>blip([var([0,-1,-1,0]),4,[7,10],9],dur=1/4, sus=1, oct=[3,4], bits=3, chop=4)

s2 >>varsaw (var([0,-2,-1.5,1],8),oct=4, chop=8, hpf=0, dur=2, rate=1 )

bd >>play ("(X[--])", amp=6,dur=0.5)
hh >>play ("-", amp=4,dur=0.25)
sn >>play ("(o )/", sus=0.1,amp=2)

b1 >>bass(var([2,1,6,4],8), dur=4, chop=(8,5), bits=(4,3), pan=(-1,1), amp=1/2)
b2 >>bass(dur=4, chop=(8,5), bits=(4,3), pan=(-1,1), amp=1/2)
b3 >>bass(([0,1.1,2,0,1.4]),chop=2, dur=0.5,rate=PRange (3)/4).solo()


s1 >>varsaw(var([0,2,6,4],8), dur=[1/2,1/2,1/4,1/2], amp=2, rate=PRange(2)/8, chop=2, pan=linvar([-1,1],12), hpf=linvar([0,4000,[32,0]])).solo()

d1 >>dab(var([0,-1,-2,2],8), dur=8, pan=(0.5,-0.5), chop=32) + (0,16)

c1 >>soprano(sus=4, oct=5, pan=(-1,1), dur=2)

s1.stop()

Clock.clear()
print (Scale.names())

Clock.bmp=120

print (SynthDefs)#imprime synth en consola

p1 >> pluck(([0,1,3,2],3), dur=[0.25], amp=[3], oct=[3])

b2 >> lazer([([0,[2,4],3,1]),4],chop=2, dur=0.5,oct=[4], pan=(-1,1), amp=(1.5)).solo()

b1 >> bass([0,2,0,1.5], dur=1/2,amp=1.5, chop=2)
p2 >> sawbass(var([0,2,1,2]),dur=2,chop=4,oct=6, amp=2).follow(b) + (0.8,1,0.7) # This adds a triad to the bass notes


d1 >> play("<-><fork>", rate=(1,4), formant=(0,[1,2,P*(3,4)]))
d2 >> play("  f f", sample=2)
d3 >> play("y ( y)", rate=2)
d4 >> play("pluck", rate=10)


p1 >> pluck(PRange(5) | PRange(5,0,-1), scale=Scale.default.pentatonic)
