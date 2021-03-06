from manimlib import *

class Optimin(GraphScene, ThreeDScene):

  CONFIG = {
    "rows":8,
    "columns":24,
    "height": FRAME_Y_RADIUS*2,
    "width": 24,
    "grid_stroke":0.1,
    "grid_color":WHITE,
    "axis_color":RED,
    "axis_stroke":2,
    "show_points":False,
    "point_radius":0,
    "labels_scale":0.5,
    "labels_buff":0,
    "number_decimals":2
  }

  def setup(self):
    ThreeDScene.setup(self)
    GraphScene.setup(self)

  def construct(self):
    # self.move_camera(phi=70*DEGREES, theta=20*DEGREES,frame_center=(-1.5,4,0))
    # self.begin_ambient_camera_rotation(rate=0.01)
    # self.setup_axes(animate=False)
    
    graph = self.get_graph(lambda x: np.cos(2*np.cos(x))*np.sin(2*np.sin(x))+2, x_min=0, x_max=TAU, color=RED) 
    
    line2 = self.get_vertical_line_to_graph(PI/2, graph, DashedLine, color=YELLOW)
    
    tma = TexMobject(r"\theta_{\text{max}}").set_color(GREEN).scale(.6).next_to(line2,DOWN,buff=SMALL_BUFF)
    hl = DashedLine( self.coords_to_point(PI/2,np.sin(2)+2), self.coords_to_point(0,np.sin(2)+2), color=YELLOW)
    
    tt = TexMobject(r"f(\theta_{\text{max}})").set_color(RED).scale(.6).next_to(hl,LEFT,buff=SMALL_BUFF)
    k = Line(self.coords_to_point(-1,-10), self.coords_to_point(-1,10), color=GREY)
    
    tt[2:6].set_color(GREEN)
    group = VGroup(k,tt,tma,line2,hl,graph, self.x_axis, self.y_axis, self.axes)
    group.scale_in_place(.7)
    group.move_to(2*RIGHT+3*UP)
    self.add_fixed_in_frame_mobjects(group)
    
    axes = ThreeDAxes()
    
    grilla=NumberPlane(width=self.width, height=self.height, rows=self.rows, columns=self.columns).set_stroke(self.grid_color, self.grid_stroke)
    grilla2=grilla.copy().next_to(grilla,UP,buff=0)
    grilla3=grilla.copy().next_to(grilla,DOWN,buff=0)
    grilla4=grilla.copy().next_to(grilla,LEFT+UP,buff=0)
    grilla5=grilla.copy().next_to(grilla,LEFT+DOWN,buff=0)
    grilla6=grilla.copy().next_to(grilla,LEFT,buff=0)
    grilla7=grilla.copy().next_to(grilla,RIGHT,buff=0)
    self.add(axes,k)

    surface=ParametricSurface(
      lambda u,v : np.array([
        u,
        v,
        np.cos(u)*np.sin(v)+2
    ]),v_min=-4,v_max=4,u_min=-4,u_max=4,checkboard_colors=[BLUE_D,BLUE_E],
    resolution=(30, 63),gloss=.9).fade(.7).set_color_by_gradient(GREEN,BLUE)
    
    curve=ParametricFunction(
      lambda u : np.array([
        2*np.cos(u),
        2*np.sin(u),
        0
      ]),color=RED,t_min=0,t_max=TAU,
    )

    curve2=ParametricFunction(
      lambda u : np.array([
          2*np.cos(u),
          2*np.sin(u),
          np.cos(2*np.cos(u))*np.sin(2*np.sin(u))+2
      ]),color=RED,t_min=0,t_max=TAU,
    )    
    
    f = TexMobject(r"z=f(x,y)").next_to(surface,Z_AXIS).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS)  
    self.add(surface,f)
    
    def arrow(u=0):
      return Arrow(np.array([
        2*np.cos(u),
        2*np.sin(u),
        0
      ]),np.array([
        2*np.cos(u),
        2*np.sin(u),
        np.cos(2*np.cos(u))*np.sin(2*np.sin(u))+2
      ]), buff=0).set_color(YELLOW)

    k=arrow()     ###### updating the curve to follow the area################

    def update_arrow(k, alpha):
      ddx = interpolate(0, TAU, alpha)
      k_k = arrow(ddx)
      k.become(k_k)

    def line(u=0):
      return DashedLine((0,0,0),(2*np.cos(u),2*np.sin(u),0)).set_color(YELLOW)

    l=line()     ###### updating the curve to follow the area################

    def update_line(l,alpha):
      dl = interpolate(0, TAU, alpha)
      ll = line(dl)
      l.become(ll) 

    def ano(dtheta=TAU):
      return Sector(inner_radius=0,outer_radius=.5,angle=dtheta,color=PURPLE,stroke_width=0).set_fill(GREEN, opacity=.8)

    cc=ano()
  
    def update_theta(cc,alpha):
      dtheta=interpolate(0,TAU,alpha)
      dt=ano(dtheta)
      cc.become(dt)
        
    theta=TexMobject(r"\theta").rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).set_color(GREEN).scale(.6)
    theta.add_updater(lambda m: m.move_to(l.get_center()+.5*UP))
    theta.shift(.1*UP)
    self.play(GrowArrow(k),ShowCreation(l),FadeIn(theta))
    self.wait(1)

    self.play(ShowCreation(graph,run_time=7),ShowCreation(curve,run_time=7),ShowCreation(curve2,run_time=7),UpdateFromAlphaFunc(k,update_arrow,run_time=7),UpdateFromAlphaFunc(l,update_line,run_time=7),UpdateFromAlphaFunc(cc,update_theta,run_time=7))
    self.wait(1)

    self.play(FadeOut(f),FadeOut(surface),FadeOut(k))
    self.wait(1)

    ft=TexMobject(r"z=f(\theta)").next_to(curve2,UP).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).set_color(RED)
    self.play(FadeIn(ft))
    self.wait(1)
    
    def update_theta2(cc,alpha):
      dtheta=interpolate(TAU,PI/2,alpha)
      dt=ano(dtheta)
      cc.become(dt)
      
    def update_line2(l,alpha):
      dl = interpolate(TAU, PI/2, alpha)
      ll = line(dl)
      l.become(ll)

    self.play(UpdateFromAlphaFunc(l,update_line2,run_time=2),UpdateFromAlphaFunc(cc,update_theta2,run_time=2))
    lz=DashedLine((0,2,0),(0,2,2.9093))
    zl=DashedLine((0,2,2.9093),(0,0,2.9093))
    self.play(ShowCreation(lz),ShowCreation(line2))
    self.play(ShowCreation(zl),ShowCreation(hl))
    z=TexMobject(r"z=f(\theta_{\text{max}})").set_color(RED).rotate(PI/2,axis=X_AXIS).rotate(PI/2,axis=Z_AXIS).scale(.6).move_to((0,-1,2.9093))
    z[4:8].set_color(GREEN)
    tm=TexMobject(r"\theta_\text{max}").set_color(GREEN).scale(.6)
    theta.clear_updaters()
    tm.move_to(.7*RIGHT+1*UP).rotate(PI/2,axis=Z_AXIS).rotate(PI/2,axis=Y_AXIS)
    self.play(Write(z),Transform(theta,tm),Write(tt),Write(tma))
    self.wait(1)
