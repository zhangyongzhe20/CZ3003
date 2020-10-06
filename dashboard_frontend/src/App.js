import React, { Component } from "react";
import { Navbar, Row, Col, Container, ToggleButton, Button, ButtonGroup } from "react-bootstrap";
import Chart from 'chart.js';
import "./styles.css";

class PieChart extends Component {
  constructor(props) {
    super(props);
    this.chartRef = React.createRef();
  }

  componentDidMount(){
    this.myChart = new Chart(this.chartRef.current, {
      type: 'pie',
      data: this.props.data,
    });
  }

  render(){
    return <canvas ref={this.chartRef} />;
  }
}

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [
        {
          "id": 0,
          "worldID_id": 0,
          "sectionID_id": 0,
          "questionID_id": 0,
          "studentID_id": 0,
          "timestamp": "2020-10-05T09:35:52.068221Z",
          "isAnsweredCorrect": true,
          "studentAnswer": "0",
          "student_email": "ii@email.com"
        }
      ],
      statistics: "Average",
    }
  }

  async componentDidMount() {
    try {
      const res = await fetch('http://127.0.0.1:8000/api/overallSummary');
      const data_json = await res.json();
      const data = data_json[0]['questionHistory'];
      this.setState({ data });
      console.log(this.state.data)
    } catch (e) {
      console.log(e);
    }
  }

  generateWorldButton() {
    if (this.state.data === undefined) {
      return null;
    }
    const worldList = this.state.data.reduce((total, value) => {
      return total.add(value.worldID_id)
    }, new Set())

    var arrButtons = [];

    const worldArray = Array.from(worldList).sort()

    for (const world of worldArray) {
      arrButtons.push(<ToggleButton type="radio" checked={this.state.world === world} onChange={() => this.setState({ world })}>
        {world}
      </ToggleButton>)
    }

    return (
      <ButtonGroup toggle>
        {arrButtons}
      </ButtonGroup>
    )
  }

  generateChart(){
    if (this.state.data === undefined){
      return null
    }
    if (this.state.world === undefined){
      return <div>
        Please select a world to check
      </div>
    }

    const filteredData = this.state.data.filter((value) => {
      return value.worldID_id === this.state.world
    })

    const correctCount = filteredData.reduce((total, value) => {
      if (value.isAnsweredCorrect){
        return total += 1;
      }
      return total;
    }, 0)

    const correctCountData = {
      datasets:[
        {data: [correctCount, filteredData.length - correctCount],
        backgroundColor:[
          'rgba(0, 255, 0, 1)',
          'rgba(255, 0, 0, 1)'
        ],
        }],
        labels:[
          'Correct',
          'Incorrect'
        ]
    }

    return (
    <>
    <Row>
    <Col>
      <h1>
        World {this.state.world} - {this.state.statistics} Accuracy
        </h1>
    </Col>
  </Row>
    <Row>
      <Col>
      <PieChart data={correctCountData}/>
      </Col>
    </Row>
    </>
    )
  }

  render() {
    return (
      <>
        <Navbar bg="dark" variant="dark">
          <Button bg="dark" variant="dark" href='http://127.0.0.1:8000'>
            Return
          </Button>
        </Navbar>
        <Container fluid className="p-5">
          <Row>
            <Col>
              <ButtonGroup toggle>
                <ToggleButton type="radio" checked={"Average" === this.state.statistics} onChange={() => this.setState({ statistics: "Average" })}>
                  Average
                    </ToggleButton>
                <ToggleButton type="radio" checked={"Max" === this.state.statistics} onChange={() => this.setState({ statistics: "Max" })}>
                  Max
                    </ToggleButton>
                <ToggleButton type="radio" checked={"Min" === this.state.statistics} onChange={() => this.setState({ statistics: "Min" })}>
                  Min
                    </ToggleButton>
              </ButtonGroup>
            </Col>
            <Col>
              {this.generateWorldButton()}
            </Col>
          </Row>
            {this.generateChart()}
        </Container>
      </>
    )
  }
}
export default App;
