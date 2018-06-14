d1 >> play('x-o-',sample=9)
bd >> play("x-o-[xx]-o(-[oo])").every([6,2], 'mirror').every(8, 'shuffle')
p1 >> pluck(P^(0,2,4,0.5), dur=1/2) #dur 1


Clock.bpm = 136

a = var([0, -2, 3],[8, 4, 4])

kl >> klank(a + [0,0,-5], sus=4)

l >> soprano(a + [2,2,-3], sus=4)

p >> py(P([(0,2)]).loop(3) | Ptri(4), dur=Psum(3,2).loop(3) | Psum(6,2), scale=Scale.major.Pentatonic, oct=(6,6,7,7)).offbeat().every(1.5, rev) + var([0,4,5,3])

bd >> bass(a, dur=Psum(7,4), sus=1)

cd >> crunch(dur=1/4)

bd $ "x  vm   "
ck $ "^tfr[/f]"
ck.rate=Pwhite(10,20)

