/**
 ******************************************************************************
 * Xenia : Xbox 360 Emulator Research Project                                 *
 ******************************************************************************
 * Copyright 2013 Ben Vanik. All rights reserved.                             *
 * Released under the BSD license - see LICENSE in the root for more details. *
 ******************************************************************************
 */

#ifndef ALLOY_BACKEND_X64_OPTIMIZER_PASSES_REGISTER_ALLOCATION_PASS_H_
#define ALLOY_BACKEND_X64_OPTIMIZER_PASSES_REGISTER_ALLOCATION_PASS_H_

#include <alloy/backend/x64/optimizer/optimizer_pass.h>


namespace alloy {
namespace backend {
namespace x64 {
namespace optimizer {
namespace passes {


class RegisterAllocationPass : public OptimizerPass {
public:
  RegisterAllocationPass();
  virtual ~RegisterAllocationPass();

  virtual int Run(lir::LIRBuilder* builder);
};


}  // namespace passes
}  // namespace optimizer
}  // namespace x64
}  // namespace backend
}  // namespace alloy


#endif  // ALLOY_BACKEND_X64_OPTIMIZER_PASSES_REGISTER_ALLOCATION_PASS_H_
