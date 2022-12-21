pelo(_).
leite(_).
penas(_).
voa(_).
botaovos(_).
comecarne(_).
dentespontudos(_).
garras(_).
olhosfrontais(_).
casco(_).
rumina(_).
dedospares(_).
coramarelotostado(_).
manchasescuras(_).
pernaslongas(_).
pescococomprido(_).
corpretoebranco(_).
nada(_).
bomvoador(_).
tamanhomedio(_).
tamanhoenorme(_).
mamifero(_) :- pelo(_).
mamifero(_) :- leite(_).
ave(_) :- penas(_).
ave(_) :- voa(_),botaovos(_).
carnivoro(_) :- mamifero(_),comecarne(_).
carnivoro(_) :- mamifero(_),dentespontudos(_),garras(_),olhosfrontais(_).
ungulado(_) :- mamifero(_),casco(_).
ungulado(_) :- mamifero(_),rumina(_),dedospares(_).
leopardo(_) :- carnivoro(_),coramarelotostado(_),manchasescuras(_).
girafa(_) :- ungulado(_),pernaslongas(_),pescococomprido(_),coramarelotostado(_),manchasescuras(_).
zebra(_) :- ungulado(_),corbranca(_),listraspretas(_).
avestruz(_) :- ave(_),pernaslongas(_),pescococomprido(_),corpretoebranco(_).
pinguim(_) :- ave(_),naovoa(_),nada(_),corpretoebranco(_).
albatroz(_) :- ave(_),bomvoador(_).
baleia(_) :- mamifero(_),nada(_),tamanhoenorme(_).
golfinho(_) :- mamifero(_),nada(_),tamanhomedio(_).
peixe(_) :- not(ave(_)),not(mamifero(_)),nada(_).              
girafa(animal)

?-mamifero(animal)