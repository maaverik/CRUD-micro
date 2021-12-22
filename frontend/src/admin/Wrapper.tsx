import React, { PropsWithChildren } from "react";

const Wrapper = (props: PropsWithChildren<any>) => {
  return (
    <div>
      <div className="container-fluid">
        <div className="row">
          <main role="main" className="col-md-9 ml-sm-auto col-lg-10 px-md-4">
            {props.children}
          </main>
        </div>
      </div>
    </div>
  );
};

export default Wrapper;
