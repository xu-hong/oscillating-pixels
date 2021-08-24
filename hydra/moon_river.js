noise(3, 0.763)
  .add(gradient(1.1))
  .luma(0.1, 0.067)
  .modulateScale(o1)
  .mask(
    shape(30, 0.1, 0.7)
     .color(1,1,0)
   )
  .out(o0);

src(o0).diff(osc().rotate(0,0.1)).out(o1);

render(o0);
