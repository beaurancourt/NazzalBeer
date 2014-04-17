from __future__ import division
from coopr.pyomo import *
from coopr.opt import *

model = ConcreteModel()

n = 26

model.n = Param(default=n)
model.max = Param(default=600)
model.M = Param(default=600)
model.index = RangeSet(model.n)
paleAleDemand = [0, 200, 260, 300, 270, 270, 280, 320, 350, 420, 600, 700, 400, 400, 400, 420, 450, 480, 410, 350, 250, 200, 300, 300, 330, 420, 450]
stoutDemand = [0, 50, 70, 80, 100, 120, 150, 150, 180, 180, 150, 150, 150, 150, 180, 240, 250, 250, 200, 200, 200, 200, 190, 200, 160, 150, 190]
# summerAleDemand = [0]*27
winterBrewDemand = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 100, 500, 200, 200, 200, 600, 200, 200, 200, 200, 300, 200, 200, 160, 120, 120, 0]
octoberfestDemand = [0, 0, 250, 250, 350, 400, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

model.paleAle1 = Var(model.index, bounds=(0, model.max))
model.paleAle2 = Var(model.index, bounds=(0, model.max))
model.paleAle3 = Var(model.index, bounds=(0, model.max))

model.paleAle1Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.paleAle2Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.paleAle3Half = Var(model.index, domain=Integers, bounds=(0, 2))

def paleAle1HalfConstraint(model, i):
  return model.paleAle1[i] == 300*model.paleAle1Half[i]
model.paleAle1HalfConstraint = Constraint(model.index, rule=paleAle1HalfConstraint)
def paleAle2HalfConstraint(model, i):
  return model.paleAle2[i] == 300*model.paleAle2Half[i]
model.paleAle2HalfConstraint = Constraint(model.index, rule=paleAle2HalfConstraint)
def paleAle3HalfConstraint(model, i):
  return model.paleAle3[i] == 300*model.paleAle3Half[i]
model.paleAle3HalfConstraint = Constraint(model.index, rule=paleAle3HalfConstraint)

model.yPaleAle1 = Var(model.index, domain=Binary)
model.yPaleAle2 = Var(model.index, domain=Binary)
model.yPaleAle3 = Var(model.index, domain=Binary)

def paleAleBin1(model, i):
  return 600 * model.yPaleAle1[i] >= model.paleAle1[i]
model.paleAleBin1Constraint = Constraint(model.index, rule=paleAleBin1)
def paleAleBin2(model, i):
  return 600 * model.yPaleAle2[i] >= model.paleAle2[i]
model.paleAleBin2Constraint = Constraint(model.index, rule=paleAleBin2)
def paleAleBin3(model, i):
  return 600 * model.yPaleAle3[i] >= model.paleAle3[i]
model.paleAleBin3Constraint = Constraint(model.index, rule=paleAleBin3)

model.stout1 = Var(model.index, bounds=(0, model.max))
model.stout2 = Var(model.index, bounds=(0, model.max))
model.stout3 = Var(model.index, bounds=(0, model.max))

model.stout1Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.stout2Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.stout3Half = Var(model.index, domain=Integers, bounds=(0, 2))

def stout1HalfConstraint(model, i):
  return model.stout1[i] == 300*model.stout1Half[i]
model.stout1HalfConstraint = Constraint(model.index, rule=stout1HalfConstraint)
def stout2HalfConstraint(model, i):
  return model.stout2[i] == 300*model.stout2Half[i]
model.stout2HalfConstraint = Constraint(model.index, rule=stout2HalfConstraint)
def stout3HalfConstraint(model, i):
  return model.stout3[i] == 300*model.stout3Half[i]
model.stout3HalfConstraint = Constraint(model.index, rule=stout3HalfConstraint)

model.yStout1 = Var(model.index, domain=Binary)
model.yStout2 = Var(model.index, domain=Binary)
model.yStout3 = Var(model.index, domain=Binary)


def stoutBin1(model, i):
  return 600 * model.yStout1[i] >= model.stout1[i]
model.stoutBin1Constraint = Constraint(model.index, rule=stoutBin1)
def stoutBin2(model, i):
  return 600 * model.yStout2[i] >= model.stout2[i]
model.stoutBin2Constraint = Constraint(model.index, rule=stoutBin2)
def stoutBin3(model, i):
  return 600 * model.yStout3[i] >= model.stout3[i]
model.stoutBin3Constraint = Constraint(model.index, rule=stoutBin3)

# model.summerAle1 = Var(model.index, within=Integers, bounds=(0, model.max))
# model.summerAle2 = Var(model.index, within=Integers, bounds=(0, model.max))
# model.summerAle3 = Var(model.index, within=Integers, bounds=(0, model.max))

# model.ySummerAle1 = Var(model.index, domain=Binary)
# model.ySummerAle2 = Var(model.index, domain=Binary)
# model.ySummerAle3 = Var(model.index, domain=Binary)

# def summerAleBin1(model, i):
#   return 600 * model.ySummerAle1[i] >= model.summerAle1[i]
# def summerAleBin2(model, i):
#   return 600 * model.ySummerAle2[i] >= model.summerAle2[i]
# def summerAleBin3(model, i):
#   return 600 * model.ySummerAle3[i] >= model.summerAle3[i]

model.winterBrew1 = Var(model.index, bounds=(0, model.max))
model.winterBrew2 = Var(model.index, bounds=(0, model.max))
model.winterBrew3 = Var(model.index, bounds=(0, model.max))

model.winterBrew1Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.winterBrew2Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.winterBrew3Half = Var(model.index, domain=Integers, bounds=(0, 2))

def winterBrew1HalfConstraint(model, i):
  return model.winterBrew1[i] == 300*model.winterBrew1Half[i]
model.winterBrew1HalfConstraint = Constraint(model.index, rule=winterBrew1HalfConstraint)
def winterBrew2HalfConstraint(model, i):
  return model.winterBrew2[i] == 300*model.winterBrew2Half[i]
model.winterBrew2HalfConstraint = Constraint(model.index, rule=winterBrew2HalfConstraint)
def winterBrew3HalfConstraint(model, i):
  return model.winterBrew3[i] == 300*model.winterBrew3Half[i]
model.winterBrew3HalfConstraint = Constraint(model.index, rule=winterBrew3HalfConstraint)

model.yWinterBrew1 = Var(model.index, domain=Binary)
model.yWinterBrew2 = Var(model.index, domain=Binary)
model.yWinterBrew3 = Var(model.index, domain=Binary)


def winterBrewBin1(model, i):
  return 600 * model.yWinterBrew1[i] >= model.winterBrew1[i]
model.winterBrewBin1Constraint = Constraint(model.index, rule=winterBrewBin1)
def winterBrewBin2(model, i):
  return 600 * model.yWinterBrew2[i] >= model.winterBrew2[i]
model.winterBrewBin2Constraint = Constraint(model.index, rule=winterBrewBin2)
def winterBrewBin3(model, i):
  return 600 * model.yWinterBrew3[i] >= model.winterBrew3[i]
model.winterBrewBin3Constraint = Constraint(model.index, rule=winterBrewBin3)

model.octoberfest1 = Var(model.index, bounds=(0, model.max))
model.octoberfest2 = Var(model.index, bounds=(0, model.max))
model.octoberfest3 = Var(model.index, bounds=(0, model.max))

model.octoberfest1Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.octoberfest2Half = Var(model.index, domain=Integers, bounds=(0, 2))
model.octoberfest3Half = Var(model.index, domain=Integers, bounds=(0, 2))

def octoberfest1HalfConstraint(model, i):
  return model.octoberfest1[i] == 300*model.octoberfest1Half[i]
model.octoberfest1HalfConstraint = Constraint(model.index, rule=octoberfest1HalfConstraint)
def octoberfest2HalfConstraint(model, i):
  return model.octoberfest2[i] == 300*model.octoberfest2Half[i]
model.octoberfest2HalfConstraint = Constraint(model.index, rule=octoberfest2HalfConstraint)
def octoberfest3HalfConstraint(model, i):
  return model.octoberfest3[i] == 300*model.octoberfest3Half[i]
model.octoberfest3HalfConstraint = Constraint(model.index, rule=octoberfest3HalfConstraint)

model.yOctoberfest1 = Var(model.index, domain=Binary)
model.yOctoberfest2 = Var(model.index, domain=Binary)
model.yOctoberfest3 = Var(model.index, domain=Binary)

def octoberfestBin1(model, i):
  return 600 * model.yOctoberfest1[i] >= model.octoberfest1[i]
model.octoberfestBin1Constraint = Constraint(model.index, rule=octoberfestBin1)
def octoberfestBin2(model, i):
  return 600 * model.yOctoberfest2[i] >= model.octoberfest2[i]
model.octoberfestBin2Constraint = Constraint(model.index, rule=octoberfestBin2)
def octoberfestBin3(model, i):
  return 600 * model.yOctoberfest3[i] >= model.octoberfest3[i]
model.octoberfestBin3Constraint = Constraint(model.index, rule=octoberfestBin3)

model.inventoryPaleAle0 = Var(model.index)
model.inventoryPaleAle1 = Var(model.index)
model.inventoryPaleAle2 = Var(model.index)
model.inventoryPaleAle3 = Var(model.index)

model.sellPaleAle0 = Var(model.index, within=NonNegativeReals)
model.sellPaleAle1 = Var(model.index, within=NonNegativeReals)
model.sellPaleAle2 = Var(model.index, within=NonNegativeReals)
model.sellPaleAle3 = Var(model.index, within=NonNegativeReals)

model.inventoryStout0 = Var(model.index, within=NonNegativeReals)
model.inventoryStout1 = Var(model.index, within=NonNegativeReals)
model.inventoryStout2 = Var(model.index, within=NonNegativeReals)
model.inventoryStout3 = Var(model.index, within=NonNegativeReals)

model.sellStout0 = Var(model.index, within=NonNegativeReals)
model.sellStout1 = Var(model.index, within=NonNegativeReals)
model.sellStout2 = Var(model.index, within=NonNegativeReals)
model.sellStout3 = Var(model.index, within=NonNegativeReals)

# model.inventorySummerAle0 = Var(model.index)
# model.inventorySummerAle1 = Var(model.index)
# model.inventorySummerAle2 = Var(model.index)
# model.inventorySummerAle3 = Var(model.index)

# model.sellSummerAle0 = Var(model.index)
# model.sellSummerAle1 = Var(model.index)
# model.sellSummerAle2 = Var(model.index)
# model.sellSummerAle3 = Var(model.index)

model.inventoryWinterBrew0 = Var(model.index)
model.inventoryWinterBrew1 = Var(model.index)
model.inventoryWinterBrew2 = Var(model.index)
model.inventoryWinterBrew3 = Var(model.index)

model.sellWinterBrew0 = Var(model.index, within=NonNegativeReals)
model.sellWinterBrew1 = Var(model.index, within=NonNegativeReals)
model.sellWinterBrew2 = Var(model.index, within=NonNegativeReals)
model.sellWinterBrew3 = Var(model.index, within=NonNegativeReals)

model.inventoryOctoberfest0 = Var(model.index)
model.inventoryOctoberfest1 = Var(model.index)
model.inventoryOctoberfest2 = Var(model.index)
model.inventoryOctoberfest3 = Var(model.index)

model.sellOctoberfest0 = Var(model.index, within=NonNegativeReals)
model.sellOctoberfest1 = Var(model.index, within=NonNegativeReals)
model.sellOctoberfest2 = Var(model.index, within=NonNegativeReals)
model.sellOctoberfest3 = Var(model.index, within=NonNegativeReals)

### Pale Ale Inventory

def balancePaleAle0(model, i):
  if i == 1:
    return model.inventoryPaleAle0[1] == 200
  elif i == 2:
    return model.inventoryPaleAle0[2] == 600
  else:
    return model.inventoryPaleAle0[i] == model.paleAle1[i-2] + model.paleAle2[i-2] + model.paleAle3[i-2]
model.balancePaleAle0Constraint = Constraint(model.index, rule=balancePaleAle0)

def balancePaleAle1(model, i):
  if i==1:
    return model.inventoryPaleAle1[1] == 0
  else:
    return model.inventoryPaleAle1[i] == model.inventoryPaleAle0[i-1] - model.sellPaleAle0[i-1]
model.balancePaleAle1Constraint = Constraint(model.index, rule=balancePaleAle1)


def balancePaleAle2(model, i):
  if i==1:
    return model.inventoryPaleAle2[1] == 0
  else:
    return model.inventoryPaleAle2[i] == model.inventoryPaleAle1[i-1] - model.sellPaleAle1[i-1]
model.balancePaleAle2Constraint = Constraint(model.index, rule=balancePaleAle2)

def balancePaleAle3(model, i):
  if i==1:
    return model.inventoryPaleAle3[1] == 0
  else:
    return model.inventoryPaleAle3[i] == model.inventoryPaleAle2[i-1] - model.sellPaleAle2[i-1]
model.balancePaleAle3Constraint = Constraint(model.index, rule=balancePaleAle3)

def sellPaleAle0Cap(model, i):
  return model.sellPaleAle0[i] <= model.inventoryPaleAle0[i]
model.sellPaleAle0CapConstraint = Constraint(model.index, rule=sellPaleAle0Cap)
def sellPaleAle1Cap(model, i):
  return model.sellPaleAle1[i] <= model.inventoryPaleAle1[i]
model.sellPaleAle1CapConstraint = Constraint(model.index, rule=sellPaleAle1Cap)
def sellPaleAle2Cap(model, i):
  return model.sellPaleAle2[i] <= model.inventoryPaleAle2[i]
model.sellPaleAle2CapConstraint = Constraint(model.index, rule=sellPaleAle2Cap)
def sellPaleAle3Cap(model, i):
  return model.sellPaleAle3[i] <= model.inventoryPaleAle3[i]
model.sellPaleAle3CapConstraint = Constraint(model.index, rule=sellPaleAle3Cap)

def sellPaleAle3Demand(model, i):
  return model.sellPaleAle3[i] <= paleAleDemand[i]
model.sellPaleAle3DemandConstraint = Constraint(model.index, rule=sellPaleAle3Demand)
def sellPaleAle2Demand(model, i):
  return model.sellPaleAle2[i] <= paleAleDemand[i] - model.sellPaleAle3[i]
model.sellPaleAle2DemandConstraint = Constraint(model.index, rule=sellPaleAle2Demand)
def sellPaleAle1Demand(model, i):
  return model.sellPaleAle1[i] <= paleAleDemand[i] - model.sellPaleAle3[i] - model.sellPaleAle2[i]
model.sellPaleAle1DemandConstraint = Constraint(model.index, rule=sellPaleAle1Demand)
def sellPaleAle0Demand(model, i):
  return model.sellPaleAle0[i] <= paleAleDemand[i] - model.sellPaleAle3[i] - model.sellPaleAle2[i] - model.sellPaleAle1[i]
model.sellPaleAle0DemandConstraint = Constraint(model.index, rule=sellPaleAle0Demand)

### Stout Inventory

def balanceStout0(model, i):
  if i == 1:
    return model.inventoryStout0[1] == 300
  elif i == 2:
    return model.inventoryStout0[2] == 0
  else:
    return model.inventoryStout0[i] == model.stout1[i-2] + model.stout2[i-2] + model.stout3[i-2]
model.balanceStout0Constraint = Constraint(model.index, rule=balanceStout0)

def balanceStout1(model, i):
  if i==1:
    return model.inventoryStout1[1] == 0
  else:
    return model.inventoryStout1[i] == model.inventoryStout0[i-1] - model.sellStout0[i-1]
model.balanceStout1Constraint = Constraint(model.index, rule=balanceStout1)

def balanceStout2(model, i):
  if i==1:
    return model.inventoryStout2[1] == 0
  else:
    return model.inventoryStout2[i] == model.inventoryStout1[i-1] - model.sellStout1[i-1]
model.balanceStout2Constraint = Constraint(model.index, rule=balanceStout2)

def balanceStout3(model, i):
  if i==1:
    return model.inventoryStout3[1] == 0
  else:
    return model.inventoryStout3[i] == model.inventoryStout2[i-1] - model.sellStout2[i-1]
model.balanceStout3Constraint = Constraint(model.index, rule=balanceStout3)

def sellStout0Cap(model, i):
  return model.sellStout0[i] <= model.inventoryStout0[i]
model.sellStout0CapConstraint = Constraint(model.index, rule=sellStout0Cap)
def sellStout1Cap(model, i):
  return model.sellStout1[i] <= model.inventoryStout1[i]
model.sellStout1CapConstraint = Constraint(model.index, rule=sellStout1Cap)
def sellStout2Cap(model, i):
  return model.sellStout2[i] <= model.inventoryStout2[i]
model.sellStout1CapConstraint = Constraint(model.index, rule=sellStout2Cap)
def sellStout3Cap(model, i):
  return model.sellStout3[i] <= model.inventoryStout3[i]
model.sellStout3CapConstraint = Constraint(model.index, rule=sellStout3Cap)

def sellStout3Demand(model, i):
  return model.sellStout3[i] <= stoutDemand[i]
model.sellStout3DemandConstraint = Constraint(model.index, rule=sellStout3Demand)
def sellStout2Demand(model, i):
  return model.sellStout2[i] <= stoutDemand[i] - model.sellStout3[i]
model.sellStout2DemandConstraint = Constraint(model.index, rule=sellStout2Demand)
def sellStout1Demand(model, i):
  return model.sellStout1[i] <= stoutDemand[i] - model.sellStout3[i] - model.sellStout2[i]
model.sellStout1DemandConstraint = Constraint(model.index, rule=sellStout1Demand)
def sellStout0Demand(model, i):
  return model.sellStout0[i] <= stoutDemand[i] - model.sellStout3[i] - model.sellStout2[i] - model.sellStout1[i]
model.sellStout0DemandConstraint = Constraint(model.index, rule=sellStout0Demand)

### SummerAle Inventory

# def balanceSummerAle0(model, i):
#   if i == 1:
#     return model.inventorySummerAle0[1] == 200
#   elif i == 2:
#     return model.inventorySummerAle0[2] == 600
#   else:
#     return model.inventorySummerAle0[i] == model.summerAle1[i-2] + model.summerAle2[i-2] + model.summerAle3[i-2]

# def balanceSummerAle1(model, i):
#   if i==1:
#     return model.inventorySummerAle1[1] == 0
#   else:
#     return model.inventorySummerAle1[i] == model.inventorySummerAle0[i-1] - model.sellSummerAle0[i-1]

# def balanceSummerAle2(model, i):
#   if i==1:
#     return model.inventorySummerAle2[1] == 0
#   else:
#     return model.inventorySummerAle2[i] == model.inventorySummerAle1[i-1] - model.sellSummerAle1[i-1]

# def balanceSummerAle3(model, i):
#   if i==1:
#     return model.inventorySummerAle3[1] == 0
#   else:
#     return model.inventorySummerAle3[i] == model.inventorySummerAle2[i-1] - model.sellSummerAle2[i-1]

# def balanceExpiredSummerAle(model, i):
#   if i==1:
#     return model.expiredSummerAle[1] == 0
#   else:
#     return model.expiredSummerAle[i] == model.inventorySummerAle3[i-1] - model.sellSummerAle3[i-1]

# def sellSummerAle0Cap(model, i):
#   return model.sellSummerAle0[i] <= model.inventorySummerAle0[i]
# def sellSummerAle1Cap(model, i):
#   return model.sellSummerAle1[i] <= model.inventorySummerAle1[i]
# def sellSummerAle2Cap(model, i):
#   return model.sellSummerAle2[i] <= model.inventorySummerAle2[i]
# def sellSummerAle3Cap(model, i):
#   return model.sellSummerAle3[i] <= model.inventorySummerAle3[i]

# def sellSummerAle3Demand(model, i):
#   return model.sellSummerAle3[i] <= summerAleDemand[i]
# def sellSummerAle2Demand(model, i):
#   return model.sellSummerAle2[i] <= summerAleDemand[i] - model.sellSummerAle3[i]
# def sellSummerAle1Demand(model, i):
#   return model.sellSummerAle1[i] <= summerAleDemand[i] - model.sellSummerAle3[i] - model.sellSummerAle2[i]
# def sellSummerAle0Demand(model, i):
#   return model.sellSummerAle0[i] <= summerAleDemand[i] - model.sellSummerAle3[i] - model.sellSummerAle2[i] - model.sellSummerAle1[i]

### WinterBrew Inventory

def balanceWinterBrew0(model, i):
  if i == 1:
    return model.inventoryWinterBrew0[1] == 0
  elif i == 2:
    return model.inventoryWinterBrew0[2] == 0
  else:
    return model.inventoryWinterBrew0[i] == model.winterBrew1[i-2] + model.winterBrew2[i-2] + model.winterBrew3[i-2]
model.balanceWinterBrew0Constraint = Constraint(model.index, rule=balanceWinterBrew0)

def balanceWinterBrew1(model, i):
  if i==1:
    return model.inventoryWinterBrew1[1] == 0
  else:
    return model.inventoryWinterBrew1[i] == model.inventoryWinterBrew0[i-1] - model.sellWinterBrew0[i-1]
model.balanceWinterBrew1Constraint = Constraint(model.index, rule=balanceWinterBrew1)

def balanceWinterBrew2(model, i):
  if i==1:
    return model.inventoryWinterBrew2[1] == 0
  else:
    return model.inventoryWinterBrew2[i] == model.inventoryWinterBrew1[i-1] - model.sellWinterBrew1[i-1]
model.balanceWinterBrew2Constraint = Constraint(model.index, rule=balanceWinterBrew2)

def balanceWinterBrew3(model, i):
  if i==1:
    return model.inventoryWinterBrew3[1] == 0
  else:
    return model.inventoryWinterBrew3[i] == model.inventoryWinterBrew2[i-1] - model.sellWinterBrew2[i-1]
model.balanceWinterBrew3Constraint = Constraint(model.index, rule=balanceWinterBrew3)

def sellWinterBrew0Cap(model, i):
  return model.sellWinterBrew0[i] <= model.inventoryWinterBrew0[i]
model.sellWinterBrew0CapConstraint = Constraint(model.index, rule=sellWinterBrew0Cap)
def sellWinterBrew1Cap(model, i):
  return model.sellWinterBrew1[i] <= model.inventoryWinterBrew1[i]
model.sellWinterBrew1CapConstraint = Constraint(model.index, rule=sellWinterBrew1Cap)
def sellWinterBrew2Cap(model, i):
  return model.sellWinterBrew2[i] <= model.inventoryWinterBrew2[i]
model.sellWinterBrew2CapConstraint = Constraint(model.index, rule=sellWinterBrew2Cap)
def sellWinterBrew3Cap(model, i):
  return model.sellWinterBrew3[i] <= model.inventoryWinterBrew3[i]
model.sellWinterBrew3CapConstraint = Constraint(model.index, rule=sellWinterBrew3Cap)

def sellWinterBrew3Demand(model, i):
  return model.sellWinterBrew3[i] <= winterBrewDemand[i]
model.sellWinterBrew3DemandConstraint = Constraint(model.index, rule=sellWinterBrew3Demand)
def sellWinterBrew2Demand(model, i):
  return model.sellWinterBrew2[i] <= winterBrewDemand[i] - model.sellWinterBrew3[i]
model.sellWinterBrew2DemandConstraint = Constraint(model.index, rule=sellWinterBrew2Demand)
def sellWinterBrew1Demand(model, i):
  return model.sellWinterBrew1[i] <= winterBrewDemand[i] - model.sellWinterBrew3[i] - model.sellWinterBrew2[i]
model.sellWinterBrew1DemandConstraint = Constraint(model.index, rule=sellWinterBrew1Demand)
def sellWinterBrew0Demand(model, i):
  return model.sellWinterBrew0[i] <= winterBrewDemand[i] - model.sellWinterBrew3[i] - model.sellWinterBrew2[i] - model.sellWinterBrew1[i]
model.sellWinterBrew0DemandConstraint = Constraint(model.index, rule=sellWinterBrew0Demand)

### Octoberfest Inventory

def balanceOctoberfest0(model, i):
  if i == 1:
    return model.inventoryOctoberfest0[1] == 0
  elif i == 2:
    return model.inventoryOctoberfest0[2] == 600
  else:
    return model.inventoryOctoberfest0[i] == model.octoberfest1[i-2] + model.octoberfest2[i-2] + model.octoberfest3[i-2]
model.balanceOctoberfest0Constraint = Constraint(model.index, rule=balanceOctoberfest0)

def balanceOctoberfest1(model, i):
  if i==1:
    return model.inventoryOctoberfest1[1] == 0
  else:
    return model.inventoryOctoberfest1[i] == model.inventoryOctoberfest0[i-1] - model.sellOctoberfest0[i-1]
model.balanceOctoberfest1Constraint = Constraint(model.index, rule=balanceOctoberfest1)

def balanceOctoberfest2(model, i):
  if i==1:
    return model.inventoryOctoberfest2[1] == 0
  else:
    return model.inventoryOctoberfest2[i] == model.inventoryOctoberfest1[i-1] - model.sellOctoberfest1[i-1]
model.balanceOctoberfest2Constraint = Constraint(model.index, rule=balanceOctoberfest2)

def balanceOctoberfest3(model, i):
  if i==1:
    return model.inventoryOctoberfest3[1] == 0
  else:
    return model.inventoryOctoberfest3[i] == model.inventoryOctoberfest2[i-1] - model.sellOctoberfest2[i-1]
model.balanceOctoberfest3Constraint = Constraint(model.index, rule=balanceOctoberfest3)

def sellOctoberfest0Cap(model, i):
  return model.sellOctoberfest0[i] <= model.inventoryOctoberfest0[i]
model.sellOctoberfest0CapConstraint = Constraint(model.index, rule=sellOctoberfest0Cap)
def sellOctoberfest1Cap(model, i):
  return model.sellOctoberfest1[i] <= model.inventoryOctoberfest1[i]
model.sellOctoberfest1CapConstraint = Constraint(model.index, rule=sellOctoberfest1Cap)
def sellOctoberfest2Cap(model, i):
  return model.sellOctoberfest2[i] <= model.inventoryOctoberfest2[i]
model.sellOctoberfest2CapConstraint = Constraint(model.index, rule=sellOctoberfest2Cap)
def sellOctoberfest3Cap(model, i):
  return model.sellOctoberfest3[i] <= model.inventoryOctoberfest3[i]
model.sellOctoberfest3CapConstraint = Constraint(model.index, rule=sellOctoberfest3Cap)

def sellOctoberfest3Demand(model, i):
  return model.sellOctoberfest3[i] <= octoberfestDemand[i]
model.sellOctoberfest3DemandConstraint = Constraint(model.index, rule=sellOctoberfest3Demand)
def sellOctoberfest2Demand(model, i):
  return model.sellOctoberfest2[i] <= octoberfestDemand[i] - model.sellOctoberfest3[i]
model.sellOctoberfest2DemandConstraint = Constraint(model.index, rule=sellOctoberfest2Demand)
def sellOctoberfest1Demand(model, i):
  return model.sellOctoberfest1[i] <= octoberfestDemand[i] - model.sellOctoberfest3[i] - model.sellOctoberfest2[i]
model.sellOctoberfest1DemandConstraint = Constraint(model.index, rule=sellOctoberfest1Demand)
def sellOctoberfest0Demand(model, i):
  return model.sellOctoberfest0[i] <= octoberfestDemand[i] - model.sellOctoberfest3[i] - model.sellOctoberfest2[i] - model.sellOctoberfest1[i]
model.sellOctoberfest0DemandConstraint = Constraint(model.index, rule=sellOctoberfest0Demand)

### Fermenters Usage
def fermenter1(model, i):
  if i == 1:
    return model.yPaleAle1[1] + model.yStout1[1] + model.yWinterBrew1[i] + model.yOctoberfest1[1] == 0
  elif i==2:
    return model.yPaleAle1[i] + model.yPaleAle1[i-1] + model.yStout1[i] + model.yStout1[i-1] + model.yWinterBrew1[i] + model.yWinterBrew1[i-1] + model.yOctoberfest1[i] + model.yOctoberfest1[i-1] <= 1
  else:
    return model.yPaleAle1[i] + model.yPaleAle1[i-1] + model.yStout1[i] + model.yStout1[i-1] + model.yStout1[i-2] + model.yWinterBrew1[i] + model.yWinterBrew1[i-1] + model.yOctoberfest1[i] + model.yOctoberfest1[i-1] <= 1
model.fermenter1Constraint = Constraint(model.index, rule=fermenter1)
def fermenter2(model, i):
  if i == 1:
    return model.yPaleAle2[1] + model.yStout2[1] + model.yWinterBrew2[i] + model.yOctoberfest2[1] == 0
  elif i==2:
    return model.yPaleAle2[i] + model.yPaleAle2[i-1] + model.yStout2[i] + model.yStout2[i-1] + model.yWinterBrew2[i] + model.yWinterBrew2[i-1] + model.yOctoberfest2[i] + model.yOctoberfest2[i-1] <= 1
  else:
    return model.yPaleAle2[i] + model.yPaleAle2[i-1] + model.yStout2[i] + model.yStout2[i-1] + model.yStout2[i-2] + model.yWinterBrew2[i] + model.yWinterBrew2[i-1] + model.yOctoberfest2[i] + model.yOctoberfest2[i-1] <= 1
model.fermenter2Constraint = Constraint(model.index, rule=fermenter2)
def fermenter3(model, i):
  if i == 1:
    return model.yPaleAle3[1] + model.yStout3[1] + model.yWinterBrew3[1] + model.yOctoberfest3[1] <= 1
  elif i==2:
    return model.yPaleAle3[i] + model.yPaleAle3[i-1] + model.yStout3[i] + model.yStout3[i-1] + model.yWinterBrew3[i] + model.yWinterBrew3[i-1] + model.yOctoberfest3[i] + model.yOctoberfest3[i-1] <= 1
  else:
    return model.yPaleAle3[i] + model.yPaleAle3[i-1] + model.yStout3[i] + model.yStout3[i-1] + model.yStout3[i-2] + model.yWinterBrew3[i] + model.yWinterBrew3[i-1] + model.yOctoberfest3[i] + model.yOctoberfest3[i-1] <= 1
model.fermenter3Constraint = Constraint(model.index, rule=fermenter3)

# model.extraSetupPaleAle1 = Var(model.index, domain=Binary)
# model.extraSetupPaleAle2 = Var(model.index, domain=Binary)
# model.extraSetupPaleAle3 = Var(model.index, domain=Binary)

# model.extraSetupStout1 = Var(model.index, domain=Binary)
# model.extraSetupStout2 = Var(model.index, domain=Binary)
# model.extraSetupStout3 = Var(model.index, domain=Binary)

# model.extraSetupWinterBrew1 = Var(model.index, domain=Binary)
# model.extraSetupWinterBrew2 = Var(model.index, domain=Binary)
# model.extraSetupWinterBrew3 = Var(model.index, domain=Binary)

# model.extraSetupOctoberfest1 = Var(model.index, domain=Binary)
# model.extraSetupOctoberfest2 = Var(model.index, domain=Binary)
# model.extraSetupOctoberfest3 = Var(model.index, domain=Binary)

### Setup Switch for Pale Ale

# def extraPaleAle1(model, i):
#   if i==1:
#     return model.extraSetupPaleAle1[1] == 0
#   elif i==2:
#     return model.extraSetupPaleAle1[2] == 0
#   elif i==3:
#     return model.extraSetupPaleAle1[3] == 0
#   else:
#     return model.extraSetupPaleAle1[i] >= model.yPaleAle1[i] - model.yPaleAle1[i-2] - model.yPaleAle1[i-3]
# model.extraPaleAle1Constraint = Constraint(model.index, rule=extraPaleAle1)

# def extraPaleAle2(model, i):
#   if i==1:
#     return model.extraSetupPaleAle2[1] == 0
#   elif i==2:
#     return model.extraSetupPaleAle2[i] >= model.yPaleAle2[i]
#   elif i==3:
#     return model.extraSetupPaleAle2[3] >= model.yPaleAle2[i]
#   else:
#     return model.extraSetupPaleAle2[i] >= model.yPaleAle2[i] - model.yPaleAle2[i-2] - model.yPaleAle2[i-3]
# model.extraPaleAle2Constraint = Constraint(model.index, rule=extraPaleAle2)

# def extraPaleAle3(model, i):
#   if i==1:
#     return model.extraSetupPaleAle3[1] >= model.yPaleAle3[1]
#   elif i==2:
#     return model.extraSetupPaleAle3[i] >= model.yPaleAle3[i]
#   elif i==3:
#     return model.extraSetupPaleAle3[3] >= model.yPaleAle3[i] - model.yPaleAle3[i-2]
#   else:
#     return model.extraSetupPaleAle3[i] >= model.yPaleAle3[i] - model.yPaleAle3[i-2] - model.yPaleAle3[i-3]
# model.extraPaleAle3Constraint = Constraint(model.index, rule=extraPaleAle3)

# ### Setup Switch for Stout

# def extraStout1(model, i):
#   if i==1:
#     return model.extraSetupStout1[1] == 0
#   elif i==2:
#     return model.extraSetupStout1[2] >= model.yStout1[i]
#   elif i==3:
#     return model.extraSetupStout1[3] == model.yStout1[i]
#   elif i==4:
#     return model.extraSetupStout1[i] >= model.yStout1[i] - model.yStout1[i-3]
#   else:
#     return model.extraSetupStout1[i] >= model.yStout1[i] - model.yStout1[i-3] - model.yStout1[i-4]
# model.extraStout1Constraint = Constraint(model.index, rule=extraStout1)

# def extraStout2(model, i):
#   if i==1:
#     return model.extraSetupStout2[1] == 0
#   elif i==2:
#     return model.extraSetupStout2[2] >= model.yStout2[i]
#   elif i==3:
#     return model.extraSetupStout2[3] == model.yStout2[i]
#   elif i==4:
#     return model.extraSetupStout2[i] >= model.yStout2[i] - model.yStout2[i-3]
#   else:
#     return model.extraSetupStout2[i] >= model.yStout2[i] - model.yStout2[i-3] - model.yStout2[i-4]
# model.extraStout2Constraint = Constraint(model.index, rule=extraStout2)

# def extraStout3(model, i):
#   if i==1:
#     return model.extraSetupStout3[1] == 0
#   elif i==2:
#     return model.extraSetupStout3[2] >= model.yStout3[i]
#   elif i==3:
#     return model.extraSetupStout3[3] == model.yStout3[i]
#   elif i==4:
#     return model.extraSetupStout3[i] >= model.yStout3[i] - model.yStout3[i-3]
#   else:
#     return model.extraSetupStout3[i] >= model.yStout3[i] - model.yStout3[i-3] - model.yStout3[i-4]
# model.extraStout3Constraint = Constraint(model.index, rule=extraStout3)

# ### Extra Setup for WinterBrew

# def extraWinterBrew1(model, i):
#   if i==1:
#     return model.extraSetupWinterBrew1[1] >= model.yWinterBrew1[1]
#   elif i==2:
#     return model.extraSetupWinterBrew1[i] >= model.yWinterBrew1[i]
#   elif i==3:
#     return model.extraSetupWinterBrew1[3] >= model.yWinterBrew1[i] - model.yWinterBrew1[i-2]
#   else:
#     return model.extraSetupWinterBrew1[i] >= model.yWinterBrew1[i] - model.yWinterBrew1[i-2] - model.yWinterBrew1[i-3]
# model.extraWinterBrew1Constraint = Constraint(model.index, rule=extraWinterBrew1)

# def extraWinterBrew2(model, i):
#   if i==1:
#     return model.extraSetupWinterBrew2[1] >= model.yWinterBrew2[1]
#   elif i==2:
#     return model.extraSetupWinterBrew2[i] >= model.yWinterBrew2[i]
#   elif i==3:
#     return model.extraSetupWinterBrew2[3] >= model.yWinterBrew2[i] - model.yWinterBrew2[i-2]
#   else:
#     return model.extraSetupWinterBrew2[i] >= model.yWinterBrew2[i] - model.yWinterBrew2[i-2] - model.yWinterBrew2[i-3]
# model.extraWinterBrew2Constraint = Constraint(model.index, rule=extraWinterBrew2)

# def extraWinterBrew3(model, i):
#   if i==1:
#     return model.extraSetupWinterBrew3[1] >= model.yWinterBrew3[1]
#   elif i==2:
#     return model.extraSetupWinterBrew3[i] >= model.yWinterBrew3[i]
#   elif i==3:
#     return model.extraSetupWinterBrew3[3] >= model.yWinterBrew3[i] - model.yWinterBrew3[i-2]
#   else:
#     return model.extraSetupWinterBrew3[i] >= model.yWinterBrew3[i] - model.yWinterBrew3[i-2] - model.yWinterBrew3[i-3]
# model.extraWinterBrew3Constraint = Constraint(model.index, rule=extraWinterBrew3)

# ### Extra Setup for Octoberfest

# def extraOctoberfest1(model, i):
#   if i==1:
#     return model.extraSetupOctoberfest1[1] >= model.yOctoberfest1[1]
#   elif i==2:
#     return model.extraSetupOctoberfest1[i] >= model.yOctoberfest1[i]
#   elif i==3:
#     return model.extraSetupOctoberfest1[3] >= model.yOctoberfest1[i] - model.yOctoberfest1[i-2]
#   else:
#     return model.extraSetupOctoberfest1[i] >= model.yOctoberfest1[i] - model.yOctoberfest1[i-2] - model.yOctoberfest1[i-3]
# model.extraOctoberfest1Constraint = Constraint(model.index, rule=extraOctoberfest1)

# def extraOctoberfest2(model, i):
#   if i==1:
#     return model.extraSetupOctoberfest2[1] >= model.yOctoberfest2[1]
#   elif i==2:
#     return model.extraSetupOctoberfest2[i] >= model.yOctoberfest2[i]
#   elif i==3:
#     return model.extraSetupOctoberfest2[3] >= model.yOctoberfest2[i] - model.yOctoberfest2[i-2]
#   else:
#     return model.extraSetupOctoberfest2[i] >= model.yOctoberfest2[i] - model.yOctoberfest2[i-2] - model.yOctoberfest2[i-3]
# model.extraOctoberfest2Constraint = Constraint(model.index, rule=extraOctoberfest2)

# def extraOctoberfest3(model, i):
#   if i==1:
#     return model.extraSetupOctoberfest3[1] >= model.yOctoberfest3[1]
#   elif i==2:
#     return model.extraSetupOctoberfest3[i] >= model.yOctoberfest3[i]
#   elif i==3:
#     return model.extraSetupOctoberfest3[3] >= model.yOctoberfest3[i] - model.yOctoberfest3[i-2]
#   else:
#     return model.extraSetupOctoberfest3[i] >= model.yOctoberfest3[i] - model.yOctoberfest3[i-2] - model.yOctoberfest3[i-3]
# model.extraOctoberfest3Constraint = Constraint(model.index, rule=extraOctoberfest3)

# ### Setup Pale Ale
# def sameSetupCostPaleAle1(model, i):
#   return model.setupPaleAle1[i] >= 150 * model.yPaleAle1[i]

# def setupCostPaleAle1(model, i):
#   if i == 1:
#     return model.setupPaleAle1[1] == 0
#   elif i == 2:
#     return model.setupPaleAle1[2] == 150 * model.yPaleAle1[2]
#   elif i == 3:
#     return model.setupPaleAle1[i] >= (1 - model.yPaleAle1[i-2]) * 250
#   else:
#     return model.setupPaleAle1[i] >= (1 - model.yPaleAle1[i-2] - model.yPaleAle1[i-3]) * 250


def obj_expression(model):
    return 6 * summation(model.sellPaleAle0) + 6 * summation(model.sellPaleAle1) + 6 * summation(model.sellPaleAle2) + 6 * summation(model.sellPaleAle3) \
    + 7 * summation(model.sellStout0) + 7 * summation(model.sellStout1) + 7 * summation(model.sellStout2) + 7 * summation(model.sellStout3) \
    + 6 * summation(model.sellWinterBrew0) + 6 * summation(model.sellWinterBrew1) + 6 * summation(model.sellWinterBrew2) + 6 * summation(model.sellWinterBrew3) \
    + 8 * summation(model.sellOctoberfest0) + 8 * summation(model.sellOctoberfest1) + 8 * summation(model.sellOctoberfest2) + 8 * summation(model.sellOctoberfest3) \
    - .02 * 3 * summation(model.inventoryPaleAle1) - .02 * 3 * summation(model.inventoryPaleAle2) - .02 * 3 * summation(model.inventoryPaleAle3) \
    - .02 * 3 * summation(model.inventoryStout1) - .02 * 3 * summation(model.inventoryStout2) - .02 * 3 * summation(model.inventoryStout3) \
    - .02 * 2 * summation(model.inventoryWinterBrew1) - .02 * 2 * summation(model.inventoryWinterBrew2) - .02 * 2 * summation(model.inventoryWinterBrew3) \
    - .02 * 3.5 * summation(model.inventoryOctoberfest1) - .02 * 3.5 * summation(model.inventoryOctoberfest2) - .02 * 3.5 * summation(model.inventoryOctoberfest2) \
    - .02 * 3.5 * (model.inventoryPaleAle0[n] - model.sellPaleAle0[n] + model.inventoryPaleAle1[n] - model.sellPaleAle1[n] + model.inventoryPaleAle2[n] - model.sellPaleAle2[n]) \
    - .02 * 3.5 * (model.inventoryStout0[n] - model.sellStout0[n] + model.inventoryStout1[n] - model.sellStout1[n] + model.inventoryStout2[n] - model.sellStout2[n]) \
    - .02 * 3.5 * (model.inventoryWinterBrew0[n] - model.sellWinterBrew0[n] + model.inventoryWinterBrew1[n] - model.sellWinterBrew1[n] + model.inventoryWinterBrew2[n] - model.sellWinterBrew2[n]) \
    - .02 * 3.5 * (model.inventoryOctoberfest0[n] - model.sellOctoberfest0[n] + model.inventoryOctoberfest1[n] - model.sellOctoberfest1[n] + model.inventoryOctoberfest2[n] - model.sellOctoberfest2[n]) \
    - 3 * summation(model.paleAle1) - 3 * summation(model.paleAle2) - 3 * summation(model.paleAle3) \
    - 3 * summation(model.stout1) - 3 * summation(model.stout2) - 3 * summation(model.stout3) \
    - 2 * summation(model.winterBrew1) - 2 * summation(model.winterBrew2) - 2 * summation(model.winterBrew3) \
    - 3.5 * summation(model.octoberfest1) - 3.5 * summation(model.octoberfest2) - 3.5 * summation(model.octoberfest3) \
    - 150 * (summation(model.yPaleAle1) + summation(model.yPaleAle2) + summation(model.yPaleAle3)) \
    - 150 * (summation(model.yStout1) + summation(model.yStout2) + summation(model.yStout3)) \
    - 150 * (summation(model.yWinterBrew1) + summation(model.yWinterBrew2) + summation(model.yWinterBrew3)) \
    - 150 * (summation(model.yOctoberfest1) + summation(model.yOctoberfest2) + summation(model.yOctoberfest3)) \
    # - 100 * (summation(model.extraSetupPaleAle1) + summation(model.extraSetupPaleAle2) + summation(model.extraSetupPaleAle3)) \
    # - 100 * (summation(model.extraSetupStout1) + summation(model.extraSetupStout2) + summation(model.extraSetupStout3)) \
    # - 100 * (summation(model.extraSetupWinterBrew1) + summation(model.extraSetupWinterBrew2) + summation(model.extraSetupWinterBrew3)) \
    # - 100 * (summation(model.extraSetupOctoberfest1) + summation(model.extraSetupOctoberfest2) + summation(model.extraSetupOctoberfest3)) \




model.OBJ = Objective(rule=obj_expression, sense=maximize)

