noise(8)
  .kaleid(6)
  .modulateScale(osc(6, 0.125, 0.05).kaleid(50))
  .mult(osc(40, 0.05, 0.3).kaleid(10), 0.25)
  .modulate(noise(1.5))
  .saturate(15)
  .posterize(1, 0.5)
  .scale(0.3)
  .out();
