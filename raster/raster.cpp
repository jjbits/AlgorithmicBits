/*
 * Triangle polygon rasterizer pixel selector
 *
 * Copyright (C) 2018 by Joon Jung
 *
 * This code is licensed under the MIT license (MIT) (http://opensource.org/licenses/MIT)
 */

#include <stdio.h>
#include <glm/glm.hpp>

class Line {
public:
  /*
   * Normal to a Line
   *   p1 = (x1, y1) p0 = (x0, y0)
   *   t = p1 - p0 = (x1 - x0, y1 - y0)
   *   n = (y1 - y, x1 - x0)
   *
   * Implicit Equation for a Line
   *   (p - p0) dot n = 0
   *   for all points p on the line
   *
   * Outward "normal" n points to the right of the ray
   * "Interior" points atr to the left of the ray
   * and have negative (p - p0) dot n values
   *
   * Decide if a point(x, y) is inside a line l
   *  l.a = v1.y - v0.y
   *  l.b = v0.x - v0.x
   *  l.c = -(l.a * v0.x + l.b * v0.y
   *  e = l.a * x + l.b * y + l.c
   *  e <= 0 inside(on the left)
   *  e > 0 outside(on the right)
   */
  glm::vec2 makeNormal(glm::vec2 const& p0, glm::vec2 const& p1)
  {

    return glm::vec2((p1.y - p0.y), (p1.x - p0.x));
  }

  Line(glm::vec2 const& p0, glm::vec2 const& p1)
  {
    a = p1.y - p0.y;
    b = p0.x - p1.x;
    c = -(a * p0.x + b * p0.y);
  }

  Line()
  {
    Line(glm::vec2(1.0f, 1.0f), glm::vec2(2.0f, 2.0f));
  }

  float getE(float const& x, float const& y)
  {
    return a * x + b * y + c;
  }

  private:
    float a, b, c;
};

// Assume 256 x 256 tile
const int XRES = 256;
const int YRES = 256;

static inline bool isInTriangle(Line& l0, Line& l1, Line& l2,
                  float const& x, float const& y)
{
  float e0, e1, e2;
  e0 = l0.getE(x, y);
  e1 = l1.getE(x, y);
  e2 = l2.getE(x, y);
  if (e0 <= 0 && e1 <= 0 && e2 <= 0)
    return true;

  return false;
}

/*
 * Just a simple looper of the frambuffer giving O(n**2)
 */
void rasterize(glm::vec2 const& v0, glm::vec2 const& v1, glm::vec2 const& v2)
{
  Line l0 = Line(v0, v1);
  Line l1 = Line(v1, v2);
  Line l2 = Line(v2, v0);

  float e0, e1, e2;
  for (int y = 0; y < YRES; y++)
    for (int x = 0; x < XRES; x++) {
      if (isInTriangle(l0, l1, l2, x, y))
        printf("(%lf, %lf) is in the triangle. \n", (float)x, (float)y);
    }
}

void testintriangle(glm::vec2 const& v0, glm::vec2 const& v1, glm::vec2 const& v2,
                    float const& x, float const& y)
{
  // Testing isInTriangle
  Line ll0 = Line(v0, v1);
  Line ll1 = Line(v1, v2);
  Line ll2 = Line(v2, v0);
  if (isInTriangle(ll0, ll1, ll2, x, y))
    printf("(%lf, %lf) is in the triangle\n", x, y);
  else
    printf("(%lf, %lf) is not in the triangle\n", x, y);
}

int main(int argc, const char** argv)
{
  printf("Triangle rasterizer example.\n");

  // Testing normal
  Line l;
  glm::vec2 p0 = glm::vec2(-1.0f, -3.0f);
  glm::vec2 p1 = glm::vec2(3.0f, 5.0f);
  glm::vec2 n = l.makeNormal(p0, p1);

  printf("n: (%lf, %lf)\n", n.x, n.y);

  // Testing e
  // Line with slope 1
  Line l1 = Line(glm::vec2(1.0f, 1.0f), glm::vec2(2.0f, 2.0f));
  float e1 = l1.getE(3, 5);
  printf("e with Line slop 1: %lf\n", e1);

  // Testing the rasterizer
  glm::vec2 v0 = glm::vec2(1.0f, 1.0f);
  glm::vec2 v1 = glm::vec2(15.0f, 1.0f);
  glm::vec2 v2 = glm::vec2(8.0f, 32.0f);

  // Test some simple points to be or not to be in the triangle
  testintriangle(v0, v1, v2, 8.0f, 18.0f);
  testintriangle(v0, v1, v2, 8.0f, 33.0f);

  rasterize(v0, v1, v2);

  return 0;
}
