%% Example code for a channel environment

clc; 
clear
close all

%% Input the channel environment

figure(1);
Imp=imread('test_channel.png');
imshow(Imp)
xL=size(Imp,1);     % width of the environment
yL=size(Imp,2);     % length of the environment
hold on
x_I=506; y_I=1836;          % start position
x_G=4066; y_G=3052;         % target position
plot(x_I, y_I, 'kp', 'MarkerSize',20, 'MarkerFaceColor','r');   % mark the start position
plot(x_G, y_G, 'kp', 'MarkerSize',20, 'MarkerFaceColor','g');   % mark the target position 

%% tunable parameters

D_search=8*13;              % searching step length
reach_thresh=10*7;          % reaching threshold
eva_radius=3*8;             % radius for optimization
colli_radius=20*4.5;        % radius for collision detection
Iterlimit = 100000;         % itertation limit

%% Initialization of the exploaring tree

V_num = 1;
num_flag=1;
lead_v = 1;
New_lead=[];
reach_v=[];
T.v(1).x = x_I;        
T.v(1).y = y_I; 
T.v(1).cost=100000000;    % cost of the starting point
T.v(1).cucost=0;          % cumulative cost of the starting point
T.v(1).parent = 0;        % parent vertex of the staring point
lead_flag=1;
     
%% Main iteration

tic

for k=0:7
    if mod(k,2)~=0
       V_rand.x = T.v(lead_v).x + 1.4142*D_search*cosd(k*45);
       V_rand.y = T.v(lead_v).y + 1.4142*D_search*sind(k*45);
    else
       V_rand.x = T.v(lead_v).x + D_search*cosd(k*45);
       V_rand.y = T.v(lead_v).y + D_search*sind(k*45);
    end
    for n=1:V_num
      if Imp(round(V_rand.y),round(V_rand.x)) == 255
        if abs(V_rand.x-T.v(n).x) + abs(V_rand.y-T.v(n).y) > (D_search-1)
            V_rand.cost = sqrt((V_rand.x-x_G)^2 + (V_rand.y-y_G)^2);
            if V_rand.cost < T.v(lead_v).cost
                T.v(lead_v).cost = V_rand.cost;
                New_lead=[V_rand.x,V_rand.y];
                num_flag=V_num+1;
            end
        end
      end
    end
end
V_num = V_num+1;
T.v(V_num).x = New_lead(1);
T.v(V_num).y = New_lead(2);
T.v(V_num).cost = T.v(lead_v).cost;
T.v(V_num).parent = V_num-1;
T.v(V_num).cucost = T.v(V_num-1).cucost+sqrt((New_lead(1)-T.v(V_num-1).x)^2 + (New_lead(2)-T.v(V_num-1).y)^2);    
lead_v = V_num;


plot([T.v(lead_v-1).x,T.v(lead_v).x],[T.v(lead_v-1).y,T.v(lead_v).y],'-b'), hold on                           % connecting normal vertexes
plot(T.v(lead_v).x, T.v(lead_v).y, 'h','MarkerEdgeColor','b', 'MarkerSize',6, 'MarkerFaceColor','b'), hold on % mark normal vertexes

% Step 1: adding new vertex

for Iter = 1:Iterlimit

if lead_flag==1 
direct_pre = atan2d(T.v(lead_v).y-T.v(lead_v-1).y,T.v(lead_v).x-T.v(lead_v-1).x)/45;
direct_pre = round(direct_pre);
num_flag=[];
New_lead_x=[];
New_lead_y=[];
mark_cost=[];
 for k = direct_pre-2:direct_pre+2
     if mod(k,2)~=0
       V_rand.x = T.v(lead_v).x + 1.4142*D_search*cosd(k*45);
       V_rand.y = T.v(lead_v).y + 1.4142*D_search*sind(k*45);
    else
       V_rand.x = T.v(lead_v).x + D_search*cosd(k*45);
       V_rand.y = T.v(lead_v).y + D_search*sind(k*45);
     end
    
     colli=0;
     for j=1:1:6
           x_search = V_rand.x + 0.5*D_search*cosd(j*60);
           y_search = V_rand.y + 0.5*D_search*sind(j*60);
              if Imp(floor(y_search),floor(x_search))==0
                   colli=colli+1;
              end
    end
     
    if Imp(round(V_rand.y),round(V_rand.x)) == 255 && colli==0
        V_rand.cost = sqrt((V_rand.x-x_G)^2 + (V_rand.y-y_G)^2);
        if V_rand.cost < T.v(lead_v).cost
             T.v(lead_v).cost = V_rand.cost;
             New_lead_x=[New_lead_x, V_rand.x];
             New_lead_y=[New_lead_y, V_rand.y];
             mark_cost=[mark_cost, V_rand.cost];
          for n=1:V_num-1
           if abs(V_rand.x-T.v(n).x) + abs(V_rand.y-T.v(n).y) < (D_search-1)
               num_flag(length(mark_cost))=0;
               break;
           else
               num_flag(length(mark_cost))=1; 
           end
          end 
        end
    end            
 end
 
 if isempty(num_flag)
     lead_flag = 0;
 else
   for flag=1:length(num_flag)
       flag_n=length(num_flag)-flag+1;
       if num_flag(flag_n)==1
           V_num = V_num+1;
           T.v(V_num).x = New_lead_x(flag_n);
           T.v(V_num).y = New_lead_y(flag_n);
           T.v(V_num).parent = V_num-1;
           T.v(V_num).cost = mark_cost(flag_n);
           T.v(V_num).cucost = T.v(V_num-1).cucost+sqrt((T.v(V_num).x-T.v(V_num-1).x)^2 + (T.v(V_num).y-T.v(V_num-1).y)^2);  
           lead_flag=1;
           lead_v = V_num;
           plot([T.v(lead_v-1).x,T.v(lead_v).x],[T.v(lead_v-1).y,T.v(lead_v).y],'-b'), hold on                              % connecting normal vertexes
           plot(T.v(lead_v).x, T.v(lead_v).y, 'h','MarkerEdgeColor','b', 'MarkerSize',6, 'MarkerFaceColor','b'), hold on;   % mark normal vertexes
           break;
       end
   end
 end
 
else
  % if cannot approching the target, then add random vertexes
  V_rand.x = rand(1)*yL;
  V_rand.y = rand(1)*xL;
  
  dist =zeros(length(T),1);
  
  for i =1: V_num
      dist(i) = abs(T.v(i).x- V_rand.x) + abs(T.v(i).y - V_rand.y);
  end
   [value, location] = min(dist);
   x_near = [T.v(location).x,T.v(location).y];

    deltax = V_rand.x-x_near(1);
    deltay = V_rand.y-x_near(2);
    
    direct_pre = atan2d(deltay,deltax)/45;
    direct_pre = round(direct_pre);
    if mod(direct_pre,2)~=0
       new(1) = x_near(1) + 1.4142*D_search*cosd(direct_pre*45);
       new(2) = x_near(2) + 1.4142*D_search*sind(direct_pre*45);
    else
       new(1) = x_near(1) + D_search*cosd(direct_pre*45);
       new(2) = x_near(2) + D_search*sind(direct_pre*45);
    end
  
   % check the vertex if it is collision-free
   if Imp(round(new(2)),round(new(1))) == 255
    lead_flag=1;
    V_num=V_num+1;
    num_flag=1;
    lead_v=V_num;
    T.v(lead_v).x = new(1);         
    T.v(lead_v).y = new(2); 
    T.v(lead_v).cost = sqrt((new(1)-x_G)^2 + (new(2)-y_G)^2);
    T.v(lead_v).cucost = T.v(location).cucost+sqrt((new(1)-x_near(1))^2 + (new(2)-x_near(2))^2);  
    T.v(V_num).parent = location;
    plot([x_near(1),T.v(lead_v).x],[x_near(2),T.v(lead_v).y],'-r'),hold on                                          % connecting random vertexes
    plot(T.v(lead_v).x, T.v(lead_v).y, 'h','MarkerEdgeColor','r', 'MarkerSize',6, 'MarkerFaceColor','r'), hold on;  % mark random vertexes
   else
       continue;
   end
end

% find the best parent vertex for the new added vertex
    v_min = T.v(V_num).parent;
    c_min = T.v(V_num).cucost;
    v_neibor = [];
    neibor_dis = [];
    r = 2*D_search;
    neighbor_count = 0;
    
    for nb = 1:1:(V_num-1)
        test_co=[T.v(nb).x,T.v(nb).y];
        test_dis=sqrt((T.v(lead_v).x-T.v(nb).x)^2 + (T.v(lead_v).y-T.v(nb).y)^2);
        if test_dis<=r
            neighbor_count = neighbor_count+1;
            v_neibor(neighbor_count)=nb;
            neibor_dis(neighbor_count)=test_dis;
        end
    end
 
    for k=1:1:neighbor_count
        if T.v(v_neibor(k)).cucost+neibor_dis(k) < c_min
            v_min = v_neibor(k);
            c_min = T.v(v_neibor(k)).cucost+neibor_dis(k);
        end
    end
     
    T.v(V_num).parent = v_min;
    T.v(V_num).cucost = c_min;   
    
% check if the new added vertex is the better parent vertex for neibor vertexes
    for k=1:1:neighbor_count
        if T.v(v_neibor(k)).cucost > neibor_dis(k) + T.v(V_num).cucost
            T.v(v_neibor(k)).parent=V_num;
            T.v(v_neibor(k)).cucost = neibor_dis(k) + T.v(V_num).cucost;
        end
    end

 % check if reaching the target
      if T.v(lead_v).cost<=reach_thresh
       reach_v=lead_v;
       break;
      end
end

%% Extract priliminary trajectory

raw_waypoint_x=[];
raw_waypoint_y=[];
w=1;
while T.v(reach_v).parent ~= 0
    start = T.v(reach_v).parent;
    lead_v(w)=start;
    raw_waypoint_x(w)=T.v(reach_v).x;
    raw_waypoint_y(w)=T.v(reach_v).y;
    w=w+1;
    
    plot(T.v(reach_v).x, T.v(reach_v).y,'-s','MarkerEdgeColor','b','MarkerSize',10,'Color','b'), hold on
    T.v(reach_v) = T.v(start);
end

lead_v=flip(lead_v);

%% Optimize the priliminary trajecotry for safety distance

new_x=[];
new_y=[];
o=1;

dist=[];
collision=[];
cost=[];
cost2=[];


for i=2:1:length(lead_v)-1
        % plot(x_current_pix(i), y_current_pix(i),'-s','MarkerEdgeColor','b','MarkerSize',7,'Color','b'), hold on
        % old_x(o) = T.v(lead_v(i)).x;
        % old_y(o) = T.v(lead_v(i)).y;
         for r=1:1:5
             for thet=1:1:18
                 x_evaluate = T.v(lead_v(i)).x+(r-1)*eva_radius*cosd(thet*20);
                 y_evaluate = T.v(lead_v(i)).y+(r-1)*eva_radius*sind(thet*20);
                 dist1=sqrt((x_evaluate-T.v(lead_v(i-1)).x)^2+(y_evaluate-T.v(lead_v(i-1)).y)^2);
                 dist2=sqrt((x_evaluate-T.v(lead_v(i+1)).x)^2+(y_evaluate-T.v(lead_v(i+1)).y)^2);
                 dist(thet)=dist1+dist2;
                 colli=0;
                 for j=1:1:18
                    x_search = x_evaluate + colli_radius*cosd(j*20);
                    y_search = y_evaluate + colli_radius*sind(j*20);
                    if Imp(floor(y_search),floor(x_search))==0
                       colli=colli+1;
                    end
                 end
                 collision(thet)=colli;
                 cost(thet)=collision(thet)*600+2*dist(thet)+5*abs(dist1-dist2)+200*r;
             end
             
             [cost_min, location]=min(cost);
             loc(r)=location;
             cost2(r)=cost_min;
         end
         [cost_g_min, r_min]=min(cost2);
         location_min = loc(r_min);
      
         x_local = T.v(lead_v(i)).x+(r_min-1)*eva_radius*cosd(location_min*20);
         y_local = T.v(lead_v(i)).y+(r_min-1)*eva_radius*sind(location_min*20);
         T.v(lead_v(i)).x = x_local;
         T.v(lead_v(i)).y = y_local;
         
         plot(x_local, y_local,'-o','MarkerFaceColor','g','MarkerSize',7,'MarkerEdgeColor','g'), hold on  % mark the optimized trajecotry points
         
         new_x=[new_x x_local];
         new_y=[new_y y_local];

   
end

new_x=[x_I,new_x,x_G];
new_y=[y_I,new_y,y_G];
line(new_x,new_y, 'Color', 'g', 'LineWidth', 2), hold on % connecting the optimized trajectory points

toc